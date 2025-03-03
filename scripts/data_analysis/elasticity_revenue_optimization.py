sales_df['date'] = pd.to_datetime(sales_df['date'])
sales_df['week'] = sales_df['date'].dt.isocalendar().week
weekly_sales = sales_df.groupby(["product_id", "week"]).agg({
    "sales": "sum",
    "price": "mean"
}).reset_index()

import numpy as np
import pandas as pd

elasticity_results = []

for product in weekly_sales["product_id"].unique():
    product_data = weekly_sales[weekly_sales["product_id"] == product].sort_values("week").copy()

    product_data.loc[:, "prev_sales"] = product_data["sales"].shift(1)
    product_data.loc[:, "prev_price"] = product_data["price"].shift(1)

    product_data = product_data.dropna().copy()

    product_data.loc[:, "percent_change_sales"] = (product_data["sales"] - product_data["prev_sales"]) / product_data["prev_sales"]
    product_data.loc[:, "percent_change_price"] = (product_data["price"] - product_data["prev_price"]) / product_data["prev_price"]

    product_data.loc[:, "elasticity"] = product_data["percent_change_sales"] / product_data["percent_change_price"]

    elasticity_results.append(product_data.loc[:, ["product_id", "week", "elasticity"]])

elasticity_df = pd.concat(elasticity_results, ignore_index=True)

