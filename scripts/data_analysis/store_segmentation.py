import pandas as pd
from sklearn.cluster import KMeans


def load_data(sales_filepath, store_filepath):
    """Loads sales and store attribute data."""
    sales_df = pd.read_csv(sales_filepath)
    store_df = pd.read_csv(store_filepath)

    # Aggregate store-level sales
    store_sales = sales_df.groupby("store_id").agg({"sales": "sum", "revenue": "sum"}).reset_index()
    return store_sales.merge(store_df, on="store_id")


def run_kmeans(df, n_clusters=3):
    """Performs K-Means clustering on store data."""
    model = KMeans(n_clusters=n_clusters, random_state=42)
    df["Cluster"] = model.fit_predict(df[["sales", "revenue", "store_size"]])
    return df


if __name__ == "__main__":
    store_data = load_data("data/Sales.csv", "data/store_cities.csv")
    segmented_stores = run_kmeans(store_data)

    segmented_stores.to_csv("reports/store_segments.csv", index=False)
    print("✅ Store Segmentation Completed! Results saved.")
