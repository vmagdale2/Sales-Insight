# Aggregate customer-level data
customer_data = sales_df.groupby("store_id").agg({
    "sales": "sum",
    "revenue": "sum"
}).reset_index()

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
customer_data["Cluster"] = kmeans.fit_predict(customer_data[["sales", "revenue"]])
