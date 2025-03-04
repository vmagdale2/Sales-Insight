import pandas as pd
import numpy as np


def load_data(filepath):
    """Loads sales transaction data."""
    return pd.read_csv(filepath, parse_dates=["date"])


def calculate_elasticity(df):
    """Computes price elasticity using % change in quantity & price."""
    df["week"] = df["date"].dt.isocalendar().week
    weekly_sales = df.groupby(["product_id", "week"]).agg({"sales": "sum", "price": "mean"}).reset_index()

    # Compute % change in price and quantity
    weekly_sales["prev_sales"] = weekly_sales.groupby("product_id")["sales"].shift(1)
    weekly_sales["prev_price"] = weekly_sales.groupby("product_id")["price"].shift(1)

    weekly_sales.dropna(inplace=True)
    weekly_sales["price_change"] = (weekly_sales["price"] - weekly_sales["prev_price"]) / weekly_sales["prev_price"]
    weekly_sales["quantity_change"] = (weekly_sales["sales"] - weekly_sales["prev_sales"]) / weekly_sales["prev_sales"]

    # Compute price elasticity
    weekly_sales["elasticity"] = weekly_sales["quantity_change"] / weekly_sales["price_change"]
    return weekly_sales[["product_id", "week", "elasticity"]]


if __name__ == "__main__":
    sales_df = load_data("data/Sales.csv")
    elasticity_results = calculate_elasticity(sales_df)

    elasticity_results.to_csv("reports/price_elasticity_results.csv", index=False)
    print("✅ Price Elasticity Analysis Completed! Results saved.")
