import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def load_data(filepath):
    """Loads transaction data."""
    return pd.read_csv(filepath, usecols=["store_id", "date", "sales", "revenue"])


def preprocess_data(df, churn_days=90):
    """Creates churn labels and features."""
    df["date"] = pd.to_datetime(df["date"])

    # Aggregate by customer
    customer_data = df.groupby("store_id").agg({
        "date": "max",
        "sales": "sum",
        "revenue": "sum"
    }).reset_index()

    # Define churn (no purchases in the last X days)
    latest_date = df["date"].max()
    customer_data["days_since_last_purchase"] = (latest_date - customer_data["date"]).dt.days
    customer_data["churn"] = (customer_data["days_since_last_purchase"] > churn_days).astype(int)

    return customer_data.drop(columns=["date"])


def train_model(df):
    """Trains a classification model for churn prediction."""
    X = df.drop(columns=["churn", "store_id"])
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    df["churn_pred"] = model.predict(X)
    return df


if __name__ == "__main__":
    sales_df = load_data("data/Sales.csv")
    processed_df = preprocess_data(sales_df)
    results_df = train_model(processed_df)

    results_df.to_csv("reports/churn_predictions.csv", index=False)
    print("✅ Churn Prediction Completed! Results saved.")
