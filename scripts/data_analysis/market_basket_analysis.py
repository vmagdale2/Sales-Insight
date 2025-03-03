# Pivot into a basket format
basket = sales_df.pivot_table(index="store_id", columns="product_id", values="sales", aggfunc="sum").fillna(0)
basket = basket.applymap(lambda x: 1 if x > 0 else 0)

# Apply Apriori algorithm
frequent_itemsets = apriori(basket, min_support=0.02, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)