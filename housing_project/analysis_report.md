# Analysis Report - Housing Dataset

## Why I chose this dataset
The housing dataset contains geographic coordinates, income and price information, and categorical features such as `ocean_proximity`.
It is well-suited to demonstrate exploratory data analysis, interactive visualization, and simple regression relationships (income vs house value).

## Two analysis questions (and answers)
### Q1: How does median house value vary with median income?
Observation: There's a clear positive relationship — higher `median_income` tends to correspond to higher `median_house_value`. A simple linear fit shows a positive slope (see scatter plot).

### Q2: Which `ocean_proximity` categories have higher median house values?
Observation: The boxplot of `median_house_value` by `ocean_proximity` displays differences across categories. Typically, locations closer to the ocean have higher median values (inspect boxplot).

## Three plots included
1. Histogram of `median_house_value` (`plots/plot_hist_median_house_value.png`)
2. Scatter of `median_income` vs `median_house_value` with linear fit (`plots/plot_scatter_income_vs_value.png`)
3. Boxplot of `median_house_value` grouped by `ocean_proximity` (`plots/plot_box_by_ocean_proximity.png`) — if available in dataset.

## Interactivity in the app
The Streamlit app contains:
- A price range slider
- A median income range slider
- A multiselect for `ocean_proximity`
- A map (if `latitude` & `longitude` exist)

## Files created
- `app.py`
- `README.md`
- `analysis_report.md`
- `requirements.txt`
- `plots/` directory with PNGs

