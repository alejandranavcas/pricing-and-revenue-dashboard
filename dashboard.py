import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="Pricing & Revenue Dashboard", layout="wide")

# Generate synthetic data
np.random.seed(42)
n = 1000
categories = ['rings', 'bracelets', 'necklaces', 'earrings']
countries = ['USA', 'UK', 'Germany', 'France', 'Canada']

df = pd.DataFrame({
    'product_id': range(1, n+1),
    'category': np.random.choice(categories, n),
    'country': np.random.choice(countries, n),
    'date': pd.date_range('2023-01-01', periods=n, freq='D')
})

# Base price per category (realistic differences)
base_prices = {
    'rings': 300,
    'bracelets': 200,
    'necklaces': 250,
    'earrings': 150
}

# Price elasticity (how sensitive demand is)
elasticity = {
    'rings': -1.2,
    'bracelets': -1.5,
    'necklaces': -1.3,
    'earrings': -1.8
}

# Generate price
df['base_price'] = df['category'].map(base_prices)
df['price'] = df['base_price'] * np.random.uniform(0.7, 1.3, n)

# Discounts
df['discount'] = np.random.choice([0, 0.1, 0.2, 0.3], n, p=[0.5, 0.2, 0.2, 0.1])

# Effective price after discount
df['final_price'] = df['price'] * (1 - df['discount'])

# Demand model (THIS is the important part)
df['quantity_sold'] = (
    200 * (df['final_price'] / df['base_price']) ** df['category'].map(elasticity)
    * np.random.uniform(0.8, 1.2, n)
)

df['quantity_sold'] = df['quantity_sold'].astype(int).clip(lower=1)

# Revenue
df['revenue'] = df['final_price'] * df['quantity_sold']

# Discount bins
df['discount_bin'] = pd.cut(df['discount'], bins=[0, 0.1, 0.2, 0.3], labels=['0-10%', '10-20%', '20-30%'])


### Calculate KPIs
total_revenue = (df['price'] * df['quantity_sold'] * (1 - df['discount'])).sum()
avg_price = df['price'].mean()
units_sold = df['quantity_sold'].sum()
discount_rate = df['discount'].mean()

# Title
st.title("Pricing & Revenue Dashboard")

st.markdown("""
**Dashboard Summary:** This interactive dashboard analyzes pricing strategies and revenue performance for a business.
Using sales data, it explores price elasticity, promotion impacts, segmentation, and trends to inform data-driven pricing decisions.
""")

############### KPI Tiles #######################
st.header("Revenue & Pricing Overview")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Revenue", f"${total_revenue:,.2f}")
with col2:
    st.metric("Average Price", f"${avg_price:,.2f}")
with col3:
    st.metric("Units Sold", f"{units_sold:,}")
with col4:
    st.metric("Discount Rate", f"{discount_rate:.2%}")

############ Price vs Demand #####################
st.header("Price vs Demand")
fig1 = px.scatter(df, x='price', y='quantity_sold', title="Price vs Quantity Sold")
st.plotly_chart(fig1)

############ Promotion Impact #####################
st.header("Promotion Impact")
revenue_with = (df['price'] * df['quantity_sold'] * (1 - df['discount'])).sum()
revenue_without = (df['price'] * df['quantity_sold']).sum()

# Discount Level vs Sales with dropdown
fig2 = go.Figure()
all_cats = ['All'] + categories
for i, cat in enumerate(all_cats):
    if cat == 'All':
        sales = df.groupby('discount_bin')['quantity_sold'].sum()
    else:
        sales = df[df['category'] == cat].groupby('discount_bin')['quantity_sold'].sum()
    fig2.add_trace(go.Bar(x=sales.index, y=sales.values, name=cat, visible=(i == 0)))

buttons = []
for i, cat in enumerate(all_cats):
    visible = [j == i for j in range(len(all_cats))]
    buttons.append(dict(label=cat, method="update", args=[{"visible": visible}, {"title": f"Discount Level vs Sales - {cat}"}]))

fig2.update_layout(
    title="Discount Level vs Sales",
    updatemenus=[dict(active=0, buttons=buttons, x=0.1, y=1.15, xanchor="left", yanchor="top")]
)

col1, col2 = st.columns(2)
with col1:
    st.write(f"Total Revenue with Discounts: ${revenue_with:,.2f}")
    st.write(f"Total Revenue without Discounts: ${revenue_without:,.2f}")
    st.markdown("""
**Chart Summary:** This bar chart displays the total quantity sold grouped by discount levels (0-10%, 10-20%, 20-30%).
Use the dropdown menu in the top-left to filter by specific product categories (rings, bracelets, necklaces, earrings) or view 'All' for combined data across categories.
It helps analyze how different discount levels impact sales volume, revealing price elasticity patterns for pricing strategy.
""")
with col2:
    st.plotly_chart(fig2)

# By Country
revenue_by_country = df.groupby('country').apply(lambda x: (x['price'] * x['quantity_sold'] * (1 - x['discount'])).sum()).reset_index()
revenue_by_country.columns = ['country', 'revenue']
fig3 = px.bar(revenue_by_country, x='country', y='revenue', title="Revenue by Country")
st.plotly_chart(fig3)

# By Category
revenue_by_category = df.groupby('category').apply(lambda x: (x['price'] * x['quantity_sold'] * (1 - x['discount'])).sum()).reset_index()
revenue_by_category.columns = ['category', 'revenue']
fig4 = px.bar(revenue_by_category, x='category', y='revenue', title="Revenue by Category")
st.plotly_chart(fig4)

# Time Trends
df['month'] = df['date'].dt.to_period('M')
monthly_revenue = df.groupby('month').apply(lambda x: (x['price'] * x['quantity_sold'] * (1 - x['discount'])).sum()).reset_index()
monthly_revenue.columns = ['month', 'revenue']
monthly_revenue['month'] = monthly_revenue['month'].astype(str)
fig5 = px.line(monthly_revenue, x='month', y='revenue', title="Monthly Revenue Trends")
st.plotly_chart(fig5)

############### Price Change Analysis #######################
st.header("Price Change Analysis")

# Average Price Over Time
avg_price_over_time = df.groupby('month')['price'].mean().reset_index()
avg_price_over_time.columns = ['month', 'price']
avg_price_over_time['month'] = avg_price_over_time['month'].astype(str)
fig6 = px.line(avg_price_over_time, x='month', y='price', title="Average Price Over Time")
st.plotly_chart(fig6)

# Sales Over Time
sales_over_time = df.groupby('month')['quantity_sold'].sum().reset_index()
sales_over_time.columns = ['month', 'quantity_sold']
sales_over_time['month'] = sales_over_time['month'].astype(str)
fig7 = px.line(sales_over_time, x='month', y='quantity_sold', title="Sales Over Time")
st.plotly_chart(fig7)
