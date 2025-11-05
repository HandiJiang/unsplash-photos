"""
Streamlit app for Housing dataset
Widgets: price range slider, income slider, ocean_proximity multiselect
Shows data table, a map (if latitude/longitude present), and three plots.
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Housing Data Explorer - Your Name", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("/mnt/data/housing.csv")

df = load_data()

st.title("Housing Data Explorer - Handi Jiang")

st.sidebar.header("Filters")
min_price = int(df['median_house_value'].min())
max_price = int(df['median_house_value'].max())
price_range = st.sidebar.slider("Price range", min_price, max_price, (min_price, max_price))
income_min = float(df['median_income'].min())
income_max = float(df['median_income'].max())
income_range = st.sidebar.slider("Median income range", float(income_min), float(income_max), (float(income_min), float(income_max)))

ocean_vals = df['ocean_proximity'].unique().tolist() if 'ocean_proximity' in df.columns else []
ocean_selected = st.sidebar.multiselect("Ocean proximity", ocean_vals, default=ocean_vals)

filtered = df[(df['median_house_value']>=price_range[0]) & (df['median_house_value']<=price_range[1]) &
              (df['median_income']>=income_range[0]) & (df['median_income']<=income_range[1])]

if 'ocean_proximity' in df.columns and ocean_selected:
    filtered = filtered[filtered['ocean_proximity'].isin(ocean_selected)]

st.markdown("### Data (filtered)")
st.dataframe(filtered.reset_index(drop=True))

col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Histogram of median_house_value")
    fig1, ax1 = plt.subplots(figsize=(6,3))
    ax1.hist(filtered['median_house_value'].dropna(), bins=30)
    ax1.set_xlabel("median_house_value")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)
with col2:
    st.markdown("#### median_income vs median_house_value")
    fig2, ax2 = plt.subplots(figsize=(6,3))
    ax2.scatter(filtered['median_income'], filtered['median_house_value'], s=10)
    coeffs = np.polyfit(filtered['median_income'].dropna(), filtered['median_house_value'].dropna(), 1)
    ax2.plot(np.sort(filtered['median_income'].dropna()), np.poly1d(coeffs)(np.sort(filtered['median_income'].dropna())))
    ax2.set_xlabel("median_income")
    ax2.set_ylabel("median_house_value")
    st.pyplot(fig2)

# Map if lat & long
if ('latitude' in df.columns) and ('longitude' in df.columns):
    st.markdown("#### Map of listings (filtered)")
    map_df = filtered.dropna(subset=['latitude','longitude'])[['latitude','longitude']]
    if not map_df.empty:
        st.map(map_df.rename(columns={'latitude':'lat','longitude':'lon'}))

st.markdown('---')
st.markdown('#### Notes')
st.markdown('This app includes interactive sliders and multiselect as required.')
