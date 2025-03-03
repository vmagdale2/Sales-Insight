from sklearn.cluster import KMeans
import numpy as np

# Calculate total sales per store
store_sales = merged_df.groupby('store_id')['sales'].sum().reset_index()

# Prepare data for KMeans
X = store_sales[['sales']]

# Initialize and fit KMeans with 3 clusters (high, medium, low)
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Add cluster labels to the store_sales DataFrame
store_sales['cluster'] = kmeans.labels_

# Map cluster labels to performance categories
performance_mapping = {
    0: 'Low',  # Assuming cluster 0 represents low performers
    1: 'Medium',# Assuming cluster 1 represents medium performers
    2: 'High'  # Assuming cluster 2 represents high performers
}
store_sales['performance_category'] = store_sales['cluster'].map(performance_mapping)

# Print the results
print(store_sales.head())

# You can further analyze the clusters, e.g., by examining the average sales within each cluster.
cluster_stats = store_sales.groupby('performance_category')['sales'].agg(['mean', 'count'])
print("\nCluster Statistics:")
cluster_stats
