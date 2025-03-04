import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(filepath):
    """Loads customer transaction data."""
    return pd.read_csv(filepath, usecols=["store_id", "product_id", "sales", "revenue"])


def preprocess_data(df):
    """Creates customer features for clustering."""
    customer_features = df.groupby("store_id").agg({
        "sales": "sum",
        "revenue": "sum",
        "product_id": "nunique"
    }).reset_index()

    customer_features.rename(columns={"product_id": "unique_products"}, inplace=True)
    return customer_features


def run_kmeans(df, n_clusters=3):
    """Runs K-Means clustering on customer data."""
    model = KMeans(n_clusters=n_clusters, random_state=42)
    df["Cluster"] = model.fit_predict(df[["sales", "revenue", "unique_products"]])
    return df


if __name__ == "__main__":
    sales_df = load_data("data/Sales.csv")
    customer_df = preprocess_data(sales_df)
    segmented_df = run_kmeans(customer_df)

    segmented_df.to_csv("reports/customer_segments.csv", index=False)
    print("✅ Customer Segmentation Completed! Results saved.")
