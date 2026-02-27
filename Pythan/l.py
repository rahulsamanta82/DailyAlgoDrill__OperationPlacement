Automating the analysis of customer data for marketing involves several steps, including data cleaning, feature extraction, trend identification, and customer segmentation. The main goals are to use purchase history and browsing behavior to segment customers into different groups, identify trends (e.g., popular products or customer lifetime value), and visualize the insights for data-driven marketing strategies.

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load customer data (assume a CSV with columns: 'customer_id', 'purchase_date', 'amount', 'product_id')
data = pd.read_csv('customer_data.csv')

# Data Cleaning
data['purchase_date'] = pd.to_datetime(data['purchase_date'])
data.dropna(inplace=True)  # Remove missing data
data = data.drop_duplicates()  # Remove duplicates

# Feature Engineering (RFM Analysis: Recency, Frequency, Monetary)
current_date = datetime.now()
rfm = data.groupby('customer_id').agg({
    'purchase_date': lambda x: (current_date - x.max()).days,  # Recency
    'customer_id': 'count',  # Frequency
    'amount': 'sum'  # Monetary
}).rename(columns={'purchase_date': 'recency', 'customer_id': 'frequency', 'amount': 'monetary'})

# Standardize RFM values for KMeans clustering
rfm_scaled = (rfm - rfm.mean()) / rfm.std()

# Customer Segmentation using KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['cluster'] = kmeans.fit_predict(rfm_scaled)

# Visualize customer segments
sns.scatterplot(x='recency', y='monetary', hue='cluster', data=rfm, palette='Set2')
plt.title('Customer Segmentation based on RFM')
plt.show()

# Trend Analysis: Popular Products
popular_products = data.groupby('product_id').agg({
    'customer_id': 'count',  # Number of purchases
    'amount': 'sum'  # Total revenue
}).rename(columns={'customer_id': 'total_purchases', 'amount': 'total_revenue'})

# Plot most popular products
top_products = popular_products.sort_values(by='total_purchases', ascending=False).head(10)
sns.barplot(x=top_products.index, y='total_purchases', data=top_products)
plt.title('Top 10 Most Popular Products')
plt.xlabel('Product ID')
plt.ylabel('Total Purchases')
plt.show()

# Automated Marketing Campaign Suggestions
def suggest_campaign(rfm_row):
    if rfm_row['cluster'] == 0:
        return 'Send loyalty program invitation'
    elif rfm_row['cluster'] == 1:
        return 'Offer discounts for re-engagement'
    elif rfm_row['cluster'] == 2:
        return 'Upsell high-value products'
    elif rfm_row['cluster'] == 3:
        return 'Target with email campaigns'
    
rfm['campaign_suggestion'] = rfm.apply(suggest_campaign, axis=1)

# Print the first 10 customers and their suggested campaigns
print(rfm[['recency', 'frequency', 'monetary', 'cluster', 'campaign_suggestion']].head(10))