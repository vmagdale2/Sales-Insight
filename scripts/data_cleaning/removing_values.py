sales_df_updated = datasets['dataset1'].dropna(subset=['price'])
sales_df_updated.isnull().sum()

missing_values_df = product_hierarchy_df[product_hierarchy_df[['product_length', 'product_depth', 'product_width']].isnull().any(axis=1)].copy()

unique_combinations = product_hierarchy_df[['hierarchy1_id', 'hierarchy2_id', 'hierarchy3_id', 'hierarchy4_id', 'hierarchy5_id']].drop_duplicates()
print(f"Number of unique hierarchy ID combinations: {len(unique_combinations)}")

missing_values_df = product_hierarchy_df[product_hierarchy_df[['product_length', 'product_depth', 'product_width']].isnull().any(axis=1)].copy()

indices_to_delete = missing_values_df.index
product_hierarchy_df_cleaned = product_hierarchy_df.drop(indices_to_delete)

print("Original DataFrame shape:", product_hierarchy_df.shape)
print("Cleaned DataFrame shape:", product_hierarchy_df_cleaned.shape)

print("\nMissing values in cleaned DataFrame:")
print(product_hierarchy_df_cleaned[['product_length', 'product_depth', 'product_width']].isnull().sum())

product_hierarchy_df_cleaned_all = product_hierarchy_df_cleaned[product_hierarchy_df_cleaned['cluster_id'].notnull()].copy()

print("Dimensions-cleaned DataFrame shape:", product_hierarchy_df_cleaned.shape)
print("Final cleaned DataFrame shape:", product_hierarchy_df_cleaned_all.shape)
print("\nMissing values in final cleaned DataFrame:")
print(product_hierarchy_df_cleaned_all[['cluster_id']].isnull().sum())

city_names_df_cleaned = city_names_df.dropna(subset=['city_id', 'city_name']).copy()
print("Original DataFrame shape:", city_names_df.shape)
print("Cleaned DataFrame shape:", city_names_df_cleaned.shape)

print("\nMissing values in cleaned DataFrame:")
print(city_names_df_cleaned[['city_id', 'city_name']].isnull().sum())

