# Data Directory Documentation

## Overview 
This directory contains all datasets used in the **Sales-Insight** project. The data is organized into different subdirectories based on its processing stage. Below is an explanation of the structure and contents. 

## 📂 data Directory Structure
```
📁 data/
│── 📄 README.md (784 B)
│── 📁 interim/
│── 📁 processed/
│── 📁 raw/
│   │── 📄 city_names.csv (867 B)
│   │── 📄 product_hierarchy.csv (46.99 KB)
│   │── 📄 product_names.csv (17.45 KB)
│   │── 📄 sales.csv (2.31 MB)
│   │── 📄 store_cities.csv (2.71 KB)
│   └── 📄 store_names.csv (3.41 KB)
└── 📁 reference/
```
## 📌 Data Sources

### 📂 1. Raw Data
- **Location:** `📂 data/raw/`
- **Description:** Original data files obtained from [source].
- **Formats:** CSV
- **Size:** X MB

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
  2. 🔍 Handle missing values
  3. 🛠️ Feature selection and transformation
  4. 💾 Export cleaned data to `📂 data/processed/`

## 🛠️ Usage Instructions
- Load datasets in Python using:
  ```python
  import pandas as pd
  df = pd.read_csv("data/processed/final_dataset.csv")

## Data Details

