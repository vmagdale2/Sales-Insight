# Data Directory Documentation

## Overview 
This directory contains all datasets used in the **Sales-Insight** project. The data is organized into different subdirectories based on its processing stage. Below is an explanation of the structure and contents. 

## 📂 data Directory Structure
```
📁 data/
│── 📄 README.md (1.64 KB)
└── 📁 raw/
    │── 📄 city_names.csv (723 B)
    │── 📄 product_hierarchy.csv (46.99 KB)
    │── 📄 product_names.csv (16.76 KB)
    │── 📄 sales.csv (2.26 MB)
    │── 📄 store_cities.csv (2.71 KB)
    └── 📄 store_names.csv (3.27 KB)
```
## 📌 Data Sources

### 📂 1. Raw Data
- **Location:** `📂 data/raw/`
- **Description:** Original data files obtained from [source].
- **Formats:** CSV
- **Size:** 2.38 MB

### 📂 2. Processed Data
- **Location:** `📂 data/processed/`
- **Description:** Cleaned and transformed datasets ready for analysis.
- **Modifications:**
  - ✅ Null values handled
  - ✅ Feature engineering applied
  - ✅ Data normalization/scaling

### 📂 4. Interim Data
- **Location:** `📂 data/interim/`
- **Description:** Temporary datasets used during transformations before finalizing.

## ⚙️ Data Preprocessing
- **Scripts Used:** `📄 scripts/data_cleaning.py`
- **Steps Taken:**
  1. 🔄 Load raw data from `📂 data/raw/`
  2. ❓ Identify missing values and handle them appropriately
  3. 📝 Format data to ensure consistency
  4. 🗑️ Remove duplicate records
  5. 🔤 Standardize text for uniformity
  6. 💾 Export cleaned data to `📂 data/processed/`

## 🛠️ Usage Instructions

Please install and load all required dictionaries for your notebook environment. To ensure you have the necessary dependencies installed, run the following command:
  ```
  !pip install pandas
  ```
```aiignore
import pandas as pd
```
The following Python script demonstrates how to load six datasets using `pandas`. Update the file paths accordingly if your datasets are stored in a different location.
```
dataset_paths = {
    "dataset1": "data/sales.csv",
    "dataset2": "data/product_hierarchy.csv",
    "dataset3": "data/store_cities.csv",
    "dataset4": "data/city_names.csv",
    "dataset5": "data/store_names.csv",
    "dataset6": "data/product_names.csv",
}

# Load datasets into pandas DataFrames
datasets = {name: pd.read_csv(path) for name, path in dataset_paths.items()}

# Display basic info for each dataset
for name, df in datasets.items():
    print(f"\n{name.upper()} - Preview:")
    print(df.head(), "\n")
    print(df.info(), "\n")
```

# Data Dictionaries

## 📊 Data Details
### Sales.csv
This csv file provides insights into product sales, revenue, stock levels, pricing, and promotional effectiveness across different stores and dates.

| Column Name              | Description                                          | Data Type |
|--------------------------|------------------------------------------------------|-----------|
| `product_id`            | The unique identifier of a product                   | String    |
| `store_id`              | The unique identifier of a store                     | String    |
| `date`                  | Sales date (YYYY-MM-DD)                              | Date      |
| `sales`                 | Sales quantity                                       | Number    |
| `revenue`               | Daily total sales revenue                            | Number    |
| `stock`                 | End of day stock quantity                            | Number    |
| `price`                 | Product sales price                                  | Number    |
| `promo_type_1`          | Type of promotion applied on channel 1              | String    |
| `promo_bin_1`           | Binned promotion rate for applied `promo_type_1`     | String    |
| `promo_type_2`          | Type of promotion applied on channel 2              | String    |
| `promo_bin_2`           | Binned promotion rate for applied `promo_type_2`     | String    |
| `promo_discount_2`      | Discount rate for applied `promo_type_2`             | Number    |
| `promo_discount_type_2` | Type of discount applied                             | String    |

## 📦 Product Attributes Dictionary
### product_hierarchy.csv 
This csv file provides details about product dimensions such as length, depth, and width, along with cluster and hierarchy IDs.

| Column Name        | Description                              | Data Type |
|--------------------|------------------------------------------|-----------|
| `product_id`      | The unique identifier of a product       | String    |
| `product_length`  | Length of the product                    | Number    |
| `product_depth`   | Depth of the product                     | Number    |
| `product_width`   | Width of the product                     | Number    |
| `cluster_id`      | The cluster identifier                   | String    |
| `hierarchy1_id`   | Level 1 hierarchy identifier             | String    |
| `hierarchy2_id`   | Level 2 hierarchy identifier             | String    |
| `hierarchy3_id`   | Level 3 hierarchy identifier             | String    |
| `hierarchy4_id`   | Level 4 hierarchy identifier             | String    |
| `hierarchy5_id`   | Level 5 hierarchy identifier             | String    |

## 🏬 Store Attributes Dictionary
### store_cities.csv 
This csv file contains information about store identifiers, types, sizes, and the corresponding city identifiers.

| Column Name    | Description                         | Data Type |
|---------------|-------------------------------------|-----------|
| `store_id`    | The unique identifier of a store   | String    |
| `storetype_id` | The type identifier of a store    | String    |
| `store_size`  | The size of the store              | Number    |
| `city_id`     | The unique identifier of a city    | String    |

## 🏷️ Product Information Dictionary
### product_names.csv
This file links product identifiers with their corresponding names, providing a mapping for easier reference and analysis.

| Column Name     | Description                      | Data Type |
|----------------|----------------------------------|-----------|
| `product_id`   | The unique identifier of a product | String    |
| `product_name` | The name of the product         | String    |

## 🏬 Store Information Dictionary
### store_names.csv 
This file associates store identifiers with their respective names, allowing for better identification and analysis of stores.

| Column Name   | Description                      | Data Type |
|--------------|----------------------------------|-----------|
| `store_id`   | The unique identifier of a store | String    |
| `store_name` | The name of the store            | String    |

## 🌆 City Information Dictionary
### city_names.csv 
This file maps city identifiers to their names, enabling geographical analysis and insights based on city-level data.

| Column Name  | Description                     | Data Type |
|-------------|---------------------------------|-----------|
| `city_id`   | The unique identifier of a city | String    |
| `city_name` | The name of the city            | String    |
