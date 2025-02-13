# dataset_paths has been redacted to prevent viewers from seeing the original path
dataset_paths = {
    "dataset1": "path/to/sales.csv",
    "dataset2": "path/to/product_hierarchy.csv",
    "dataset3": "path/to/store_cities.csv",
    "dataset4": "path/to/city_names.csv",
    "dataset5": "path/to/store_names.csv",
    "dataset6": "path/to/product_names.csv",
}

datasets = {}
for name, path in dataset_paths.items():
    try:
        df = pd.read_csv(path)
        datasets[name] = df
        print(f"\n{name.upper()} - Preview:")
        print(df.head())
        print(df.info())
        print(df.describe())
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        datasets[name] = None
    except pd.errors.EmptyDataError:
        print(f"Error: The CSV file at {path} is empty.")
        datasets[name] = None
    except pd.errors.ParserError:
        print(f"Error: Could not parse the CSV file at {path}. Check the file format.")
        datasets[name] = None
    except Exception as e:
        print(f"An unexpected error occurred while reading {name}: {e}")
        datasets[name] = None

# dataset_paths has been redacted to prevent viewers from seeing the original path
dataset_paths = {
    "dataset1": "path/to/sales.csv",
    "dataset2": "path/to/product_hierarchy.csv",
    "dataset3": "path/to/store_cities.csv",
    "dataset4": "path/to/city_names.csv",
    "dataset5": "path/to/store_names.csv",
    "dataset6": "path/to/product_names.csv",
}

try:
    sales_df = pd.read_csv(dataset_paths["dataset1"])
    print(sales_df.head())
except FileNotFoundError:
    print(f"Error: File not found at {dataset_paths['dataset1']}")
except pd.errors.EmptyDataError:
    print(f"Error: The CSV file at {dataset_paths['dataset1']} is empty.")
except pd.errors.ParserError:
    print(f"Error: Could not parse the CSV file at {dataset_paths['dataset1']}. Check the file format.")
except Exception as e:
    print(f"An unexpected error occurred while reading dataset1: {e}")

try:
    product_hierarchy_df = pd.read_csv(dataset_paths["dataset2"])
    print(product_hierarchy_df.head())
except FileNotFoundError:
    print(f"Error: File not found at {dataset_paths['dataset2']}")
except pd.errors.EmptyDataError:
    print(f"Error: The CSV file at {dataset_paths['dataset2']} is empty.")
except pd.errors.ParserError:
    print(f"Error: Could not parse the CSV file at {dataset_paths['dataset2']}. Check the file format.")
except Exception as e:
    print(f"An unexpected error occurred while reading dataset2: {e}")

try:
    store_cities_df = pd.read_csv(dataset_paths["dataset3"])
    print(store_cities_df.head())
except FileNotFoundError:
    print(f"Error: File not found at {dataset_paths['dataset3']}")
except pd.errors.EmptyDataError:
    print(f"Error: The CSV file at {dataset_paths['dataset3']} is empty.")
except pd.errors.ParserError:
    print(f"Error: Could not parse the CSV file at {dataset_paths['dataset3']}. Check the file format.")
except Exception as e:
    print(f"An unexpected error occurred while reading dataset3: {e}")

try:
    city_names_df = pd.read_csv(dataset_paths["dataset4"])
    print(city_names_df.head())
except FileNotFoundError:
    print(f"Error: File not found at {dataset_paths['dataset4']}")
except pd.errors.EmptyDataError:
    print(f"Error: The CSV file at {dataset_paths['dataset4']} is empty.")
except pd.errors.ParserError:
    print(f"Error: Could not parse the CSV file at {dataset_paths['dataset4']}. Check the file format.")
except Exception as e:
    print(f"An unexpected error occurred while reading dataset4: {e}")

try:
    store_names_df = pd.read_csv(dataset_paths["dataset5"])
    print(store_names_df.head())
except FileNotFoundError:
    print(f"Error: File not found at {dataset_paths['dataset5']}")
except pd.errors.EmptyDataError:
    print(f"Error: The CSV file at {dataset_paths['dataset5']} is empty.")
except pd.errors.ParserError:
    print(f"Error: Could not parse the CSV file at {dataset_paths['dataset5']}. Check the file format.")
except Exception as e:
    print(f"An unexpected error occurred while reading dataset5: {e}")

try:
    product_names_df = pd.read_csv(dataset_paths["dataset6"])
    print(product_names_df.head())
except FileNotFoundError:
    print(f"Error: File not found at {dataset_paths['dataset6']}")
except pd.errors.EmptyDataError:
    print(f"Error: The CSV file at {dataset_paths['dataset6']} is empty.")
except pd.errors.ParserError:
    print(f"Error: Could not parse the CSV file at {dataset_paths['dataset6']}. Check the file format.")
except Exception as e:
    print(f"An unexpected error occurred while reading dataset6: {e}")