# Pricing & Revenue Dashboard

A Streamlit-based dashboard for analyzing pricing strategies and revenue insights using synthetic jewelry sales data (rings, bracelets, necklaces, earrings).

## Features

- **Revenue & Pricing Overview**: KPI tiles showing total revenue, average price, units sold, and discount rate.
- **Price vs Demand Scatter Plot**: Visualizes price elasticity by plotting price against quantity sold.
- **Promotion Impact Analysis**: Compares revenue with/without discounts and a bar chart of sales by discount levels, filterable by category.
- **Segmentation**: Revenue breakdowns by country and product category.
- **Time Trends**: Monthly revenue trends.
- **Price & Sales Over Time**: Line charts tracking price and sales evolution.

## Insights

### 1. Revenue & Pricing Overview

- Total revenue reflects the overall business performance after discounts.
- Average price indicates pricing strategy; higher averages suggest premium positioning.
- Units sold shows demand volume.
- Discount rate highlights promotion frequency—higher rates may boost short-term sales but impact margins.

### 2. Price vs Demand

- Demonstrates price elasticity: steeper slopes indicate higher sensitivity to price changes.
- Categories like earrings (high elasticity) show more sales variation with price, while rings (lower elasticity) are less affected.
- Helps identify optimal pricing points to maximize revenue.

### 3. Promotion Impact

- Revenue comparison shows discount effectiveness; significant drops with discounts suggest over-discounting.
- Sales by discount level reveals patterns: moderate discounts (10-20%) often drive the most volume without eroding value.
- Category filtering allows targeted promotion analysis—e.g., bracelets may respond better to discounts than rings.

### 4. Segmentation

- **By Country**: Identifies top markets (e.g., USA/UK vs. others) for localization strategies.
- **By Category**: Rings and necklaces may generate higher revenue due to pricing, while earrings sell in higher volumes.
- Informs inventory and marketing focus.

### 5. Time Trends

- Monthly revenue trends reveal seasonality or growth patterns.
- Consistent upward trends indicate successful strategies; dips may signal external factors or pricing issues.

### 6. Price & Sales Over Time

- Price trends show dynamic pricing; stable prices suggest consistent strategy.
- Sales trends correlate with promotions or market changes.
- Combined analysis highlights elasticity over time—e.g., sales spikes post-price drops.

## Screenshots

### Full Dashboard

![Full Dashboard](screenshots/full_dashboard.png)
_Overview of all sections with KPI tiles and charts._

### Price vs Demand

![Price vs Demand](screenshots/price_demand.png)
_Scatter plot showing price elasticity across categories._

### Promotion Impact

![Promotion Impact](screenshots/promotion_impact.png)
_Revenue comparison and discount level analysis with category dropdown._

### Segmentation

![Segmentation](screenshots/segmentation.png)
_Bar charts for revenue by country and category._

### Time Trends

![Time Trends](screenshots/time_trends.png)
_Monthly revenue line chart._

### Price & Sales Over Time

![Price Sales Time](screenshots/price_sales_time.png)
_Dual line charts for price and sales evolution._

_Note: Add actual screenshots to the `screenshots/` folder and update paths as needed._

## Data

Uses synthetic data with 1000 records including product ID, category, price, quantity sold, discount, date, and country. Incorporates realistic price elasticity for authentic insights.
