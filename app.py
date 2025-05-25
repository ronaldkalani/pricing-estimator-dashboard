
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv('Cleaned_Superstore_Pricing.csv')

# Preprocessing
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# Streamlit App
st.set_page_config(page_title="Pricing & Estimating Dashboard", layout="wide")
st.title("📊 Pricing & Estimating Dashboard")
st.markdown("An interactive dashboard for estimating quotes, analyzing costs, and supporting pricing decisions.")

# Sidebar filters
st.sidebar.header("🔍 Filter Options")
category = st.sidebar.selectbox("Select Category", df['Category'].unique())
region = st.sidebar.selectbox("Select Region", df['Region'].unique())
subcat_options = df[df['Category'] == category]['Sub-Category'].unique()
sub_category = st.sidebar.selectbox("Select Sub-Category", subcat_options)

filtered_df = df[(df['Category'] == category) & 
                 (df['Region'] == region) & 
                 (df['Sub-Category'] == sub_category)]

# Show summary metrics
st.subheader("Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Sales Price", f"${filtered_df['Sales'].mean():.2f}")
col2.metric("Avg. Estimated Cost", f"${filtered_df['Estimated Cost'].mean():.2f}")
col3.metric("Profit Margin %", f"{filtered_df['Profit Margin %'].mean():.2f}%")

# Quote Estimator
st.subheader("📦 Quoting Tool")
qty = st.slider("Select Quantity", 1, 1000, 10)

unit_cost = filtered_df['Estimated Cost'].mean()
unit_margin = filtered_df['Profit Margin %'].mean()
total_cost = qty * unit_cost
quote_price = total_cost * (1 + unit_margin / 100)

st.write(f"💰 Estimated Total Cost: **${total_cost:,.2f}**")
st.write(f"💡 Recommended Quote Price: **${quote_price:,.2f}**")

# Visuals Section
st.subheader("📈 Profit & Sales Breakdown")

# Bar Chart: Monthly Sales
monthly_sales = df.groupby('Month')['Sales'].sum()
fig1, ax1 = plt.subplots()
monthly_sales.plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_title('Monthly Sales Volume')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales ($)')
st.pyplot(fig1)

# Pie Chart: Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()
fig2, ax2 = plt.subplots()
ax2.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=90)
ax2.set_title('Sales Distribution by Region')
st.pyplot(fig2)

# Show Data
with st.expander("📄 View Filtered Data"):
    st.dataframe(filtered_df[['Order Date', 'Sales', 'Estimated Cost', 'Profit', 'Profit Margin %']])
