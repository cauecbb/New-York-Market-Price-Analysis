import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load all the data
df = pd.read_csv('data/newyork-housing-market.csv')

# Calculate the price per sqft for each property
df['PRICE_PER_SQFT'] = df['PRICE'] / df['PROPERTYSQFT']

# Calculate the average price per sqft for each locality
locality_avg_price = df.groupby('LOCALITY')['PRICE_PER_SQFT'].mean().reset_index()
locality_avg_price.columns = ['LOCALITY', 'AVG_PRICE_PER_SQFT']

df = df.merge(locality_avg_price, on='LOCALITY', how='left')

st.title("Price per Sqft Analysis by Locality")

st.subheader("Data Table Overview")
st.dataframe(df[['LOCALITY', 'PRICE', 'PROPERTYSQFT', 'PRICE_PER_SQFT', 'AVG_PRICE_PER_SQFT']])

# Chart 1: Price per sqft distribution
st.subheader("Price per Sqft Distribution (Overall)")
plt.figure(figsize=(10, 6))
sns.histplot(df['PRICE_PER_SQFT'], kde=True, bins=30, color='blue')
plt.title("Price per Sqft Distribution")
plt.xlabel("Price per Sqft")
plt.ylabel("Frequency")
st.pyplot(plt.gcf())

# Chart 2: Comparison of average price per locality
st.subheader("Average Price per Sqft by Locality")
plt.figure(figsize=(12, 8))
sns.barplot(
    data=locality_avg_price.sort_values(by='AVG_PRICE_PER_SQFT', ascending=False),
    x='LOCALITY', y='AVG_PRICE_PER_SQFT', palette='viridis'
)
plt.xticks(rotation=45)
plt.title("Average Price per Sqft by Locality")
plt.xlabel("Locality")
plt.ylabel("Average Price per Sqft")
st.pyplot(plt.gcf())

# Chart 3: Interactive analysis (Select a specific locality)
st.subheader("Specific Locality Analysis")
selected_locality = st.selectbox("Select a Locality", df['LOCALITY'].unique())
locality_data = df[df['LOCALITY'] == selected_locality]

st.write(f"Detailed analysis for locality: {selected_locality}")
st.dataframe(locality_data[['ADDRESS', 'PRICE', 'PROPERTYSQFT', 'PRICE_PER_SQFT']])

# Price per sqft distribution within the selected locality
plt.figure(figsize=(10, 6))
sns.histplot(locality_data['PRICE_PER_SQFT'], kde=True, bins=20, color='green')
plt.title(f"Price per Sqft Distribution in {selected_locality}")
plt.xlabel("Price per Sqft")
plt.ylabel("Frequency")
st.pyplot(plt.gcf())

