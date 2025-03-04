import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import fpgrowth, association_rules


def load_data(filepath):
    """Loads sales transaction data."""
    return pd.read_csv(filepath, usecols=["store_id", "product_id", "sales"])


def preprocess_data(df):
    """Filters top products and converts transactions to a Boolean matrix."""
    top_products = df.groupby("product_id")["sales"].sum().nlargest(1000).index
    df = df[df["product_id"].isin(top_products)]

    basket_df = df.pivot_table(index="store_id", columns="product_id", values="sales", aggfunc="sum").fillna(0)
    return basket_df > 0  # Convert to Boolean


def run_fpgrowth(basket_df, min_support=0.1):
    """Runs FP-Growth on transaction data."""
    return fpgrowth(basket_df, min_support=min_support, use_colnames=True)


def generate_rules(frequent_itemsets):
    """Generates association rules based on lift metric."""
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    return rules[rules["antecedents"].apply(lambda x: len(x) == 1) & rules["consequents"].apply(lambda x: len(x) == 1)]


if __name__ == "__main__":
    sales_df = load_data("data/Sales.csv")
    basket_df = preprocess_data(sales_df)
    frequent_itemsets = run_fpgrowth(basket_df)
    rules = generate_rules(frequent_itemsets)

    rules.to_csv("reports/market_basket_rules.csv", index=False)
    print("✅ Market Basket Analysis Completed! Results saved.")
