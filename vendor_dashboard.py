import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Vendor Analysis Dashboard")
df = pd.read_csv('vendor_data_cleaned.csv')

# Sidebar filters
region_filter = st.sidebar.multiselect("Select Regions (Countries)", df['region'].unique(), default=df['region'].unique())
category_filter = st.sidebar.multiselect("Select Categories (Vendor Types)", df['product_category'].unique(), default=df['product_category'].unique())
tier_filter = st.sidebar.multiselect("Select Tiers", df['vendor_tier'].unique(), default=df['vendor_tier'].unique())

filtered_df = df[df['region'].isin(region_filter) & df['product_category'].isin(category_filter) & df['vendor_tier'].isin(tier_filter)]

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Vendors", len(filtered_df))
col2.metric("Avg Performance", filtered_df['performance_score'].mean().round(2))
col3.metric("Avg Rating", filtered_df['rating'].mean().round(2))
col4.metric("Avg Total Spend", filtered_df['Total Spend'].mean().round(2))

# Visuals
fig_scatter = px.scatter(filtered_df, x='num_transactions', y='num_complaints', color='vendor_tier', 
                         hover_data=['Legal Company Name'])
st.plotly_chart(fig_scatter, use_container_width=True)

fig_box = px.box(filtered_df, x='region', y='performance_score')
st.plotly_chart(fig_box, use_container_width=True)
