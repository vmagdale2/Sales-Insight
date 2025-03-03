# Sales-Insight
Project outlines how I identified key factors influencing sales for an undisclosed company.

# Sales Insights: Discovering Influences through Data

## Project Description

In order for [undisclosed] company to maintain its competitive edge and optimize business performance, the company appointed me to disclose insights so that they can enhance sales strategies and operational efficiency. 

## Objectives

## Data

### Dataset Overview 
Due to confidentiality, the data is heavily redacted. The data used for this project consists of sales data containing the hierarchy and sizes of the company's products and locations. 
See the [Data README](data/README.md) for a detailed breakdown of datasets and sources. 

## Data Cleaning Process

To ensure data quality, I performed multiple cleaning steps:
1. **Missing Values**: Removed missing values. Applied contingency tables, chi-squared tests and Cramer's V to determine whether to impute or remove. 
   2. 710 missing sales values were removed
   3. 18, 16, and 16 missing product dimensions were removed
   4. 50 missing cluster_id's were removed
2. **Duplicates**: Removed 49,289 duplicates. 
3. **Inconsistent Formats**: Standardized `date` format from `MM/DD/YYYY` to `YYYY-MM-DD`.
4. **Standardized Text**: Trimmed the data to removed leading and extra spaces, ensuring text data is uniformly formatted. 

The cleaned datasets can be reviewed in the ['processed'](data/processed) folder.

Please view the interim spreadsheets in the ['interim'](data/interim) directory for review as necessary. 

For more information, please review the ['data/README.md'](data/README.md) file. 

### Code & Reproducibility 
For detailed steps, please refer to the ['Data_Cleaning_Public.ipynb](notebooks/Data_Cleaning_Public.ipynb) notebook. 

If you wish to review the scripts used to perform the cleaning steps individually, please refer to the ['scripts/data_cleaning'](scripts/data_cleaning) directory. 

## Store & Product Performance Segmentation 🏬📊

### 📌 Overview
This project identifies **high-performing stores & products** and clusters them using **K-Means Clustering**.

### 📂 Project Structure
- `notebooks/3_store_segmentation.ipynb`: Notebook with analysis & visualization.
- `scripts/store_segmentation.py`: Python script for automated clustering.
- `reports/store_segmentation_report.pdf`: Summary report with store insights.

## Stock Optimization & Demand Forecasting 📉

### 📌 Overview
This project predicts **future sales trends** and helps optimize stock replenishment using **time series forecasting**.

### 📂 Project Structure
- `notebooks/2_stock_forecasting.ipynb`: Jupyter Notebook with full analysis.
- `scripts/stock_forecasting.py`: Python script for automated forecasting.
- `reports/stock_forecasting_report.pdf`: Summary report with insights.

## Price Elasticity of Demand & Revenue Optimization 📊

### 📌 Overview
This project calculates **price elasticity** for products to optimize pricing strategies and maximize revenue.

### 📂 Project Structure
- `notebooks/1_price_elasticity.ipynb`: Jupyter Notebook with detailed analysis.
- `scripts/price_elasticity.py`: Python script for automated computation.
- `reports/price_elasticity_results.csv`: Elasticity data.
- `reports/elasticity_distribution.png`: Elasticity histogram.