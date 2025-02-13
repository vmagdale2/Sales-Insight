for name, df in datasets.items():
    if df is not None:
        num_rows = df.shape[0]
        num_columns = df.shape[1]
        print(f"\n{name.upper()} - Dimensions:")
        print(f"Number of rows: {num_rows}")
        print(f"Number of columns: {num_columns}")
    else:
        print(f"\n{name.upper()} - Dimensions: Could not be determined due to file error.")