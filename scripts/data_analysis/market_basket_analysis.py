import pandas as pd
import numpy as np
from dask.distributed import Client
from mlxtend.frequent_patterns import fpgrowth, association_rules
import dask.dataframe as dd

from google.colab import drive
drive.mount('/content/drive')

# ✅ Start Parallel Processing to Handle Large Data
client = Client()

# ✅ Load Data (Keep Only Essential Columns)
sales_df = dd.read_csv('redacted.csv', usecols=["store_id", "product_id", "sales"])

# ✅ Ensure `product_id` is a Categorical Variable
sales_df["product_id"] = sales_df["product_id"].astype("category")

# ✅ Explicitly Define Categories (This Prevents Errors)
sales_df = sales_df.categorize(columns=["product_id"])

# ✅ Filter for Top-Selling Products
top_products = sales_df.groupby("product_id")["sales"].sum().nlargest(15).index.compute()
sales_df = sales_df[sales_df["product_id"].isin(top_products)]

# ✅ Convert Dask DataFrame to Pandas for Faster Pivot Processing
sales_df = sales_df.compute()

# ✅ Create Pivot Table for Transaction Data (Store vs. Products)
basket_df = sales_df.pivot_table(index="store_id", columns="product_id", values="sales", aggfunc="sum").fillna(0)

# ✅ Convert to Boolean Matrix (1 if purchased, 0 if not)
basket_df = basket_df > 0

# ✅ Run FP-Growth Algorithm (Much Faster than Apriori)
frequent_itemsets = fpgrowth(basket_df, min_support=0.1, use_colnames=True)

# ✅ Generate Association Rules (Keep Only Product Pairs)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules = rules[rules["antecedents"].apply(lambda x: len(x) == 1) & rules["consequents"].apply(lambda x: len(x) == 1)]

# ✅ Save Results
rules.to_csv("market_basket_rules.csv", index=False)

# ✅ Display First Few Rules
print(rules.head())