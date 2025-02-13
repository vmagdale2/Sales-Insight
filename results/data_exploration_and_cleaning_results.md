# Data Cleaning and Preparation

## Tasks completed for all CSVs:
- Import data
- Explore data
- Identify missing values
- Format data
- Remove duplicates
- Standardize text

### Libraries used

```
!pip install pandas
!pip install squarify
!pip install pandas gdown
import gdown
import matplotlib.patches as mpatches
import matplotlib.cm as cm
import squarify
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from scipy.stats import chi2_contingency
from google.colab import drive

drive.mount('/content/drive')
```
## Dataset Creations
Definitions

```
DATASET1 = sales.csv
DATASET2 = product_hierarchy.csv
DATASET3 = store_cities.csv
DATASET4 = city_names.csv
DATASET5 = store_names.csv
DATASET6 = product_names.csv
```
Dataframes
```
sales_df
product_hierarchy_df
store_cities_df
city_names_df
store_names_df
product_names_df
```
# Data Exploration

## Number of rows & columns

| Dataset | Spreadsheet Name | Number of Rows | Number of Columns |
|---|---|---|---|
| DATASET1 | sales.csv | 49999 | 13 |
| DATASET2 | product_hierarchy.csv | 699 | 10 |
| DATASET3 | store_cities.csv | 144 | 4 |
| DATASET4 | city_names.csv | 144 | 2 |
| DATASET5 | store_names.csv | 144 | 2 |
| DATASET6 | product_names.csv | 699 | 2 |

## Data Types

<table>
  <tr>
    <td>
      <h2>sales.csv</h2>
      <table>
        <thead>
          <tr>
            <th>Column Name</th>
            <th>Data Type</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>product_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>store_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>date</td>
            <td>object</td>
          </tr>
          <tr>
            <td>sales</td>
            <td>float64</td>
          </tr>
          <tr>
            <td>revenue</td>
            <td>float64</td>
          </tr>
          <tr>
            <td>stock</td>
            <td>float64</td>
          </tr>
          <tr>
            <td>price</td>
            <td>float64</td>
          </tr>
          <tr>
            <td>promo_type_1</td>
            <td>object</td>
          </tr>
          <tr>
            <td>promo_bin_1</td>
            <td>object</td>
          </tr>
          <tr>
            <td>promo_type_2</td>
            <td>object</td>
          </tr>
          <tr>
            <td>promo_bin_2</td>
            <td>float64</td>
          </tr>
          <tr>
            <td>promo_discount_2</td>
            <td>float64</td>
          </tr>
          <tr>
            <td>promo_discount_type_2</td>
            <td>float64</td>
          </tr>
        </tbody>
      </table>
    </td>
    <td>
      <h2>product_hierarchy.csv</h2>
      <table>
        <thead>
          <tr>
            <th>Column Name</th>
            <th>Data Type</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>product_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>product_length</td>
            <td>float64</td>
          </tr>
          <tr>
            <td>product_depth</td>
            <td>float64</td>
          </tr>
          <tr>
            <td>product_width</td>
            <td>float64</td>
          </tr>
          <tr>
            <td>cluster_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>hierarchy1_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>hierarchy2_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>hierarchy3_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>hierarchy4_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>hierarchy5_id</td>
            <td>object</td>
          </tr>
        </tbody>
      </table>
    </td>
    <td>
      <h2>store_cities.csv</h2>
      <table>
        <thead>
          <tr>
            <th>Column Name</th>
            <th>Data Type</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>store_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>storetype_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>store_size</td>
            <td>int64</td>
          </tr>
          <tr>
            <td>city_id</td>
            <td>object</td>
          </tr>
        </tbody>
      </table>
    </td>
  </tr>
  <tr>
    <td>
      <h2>city_names.csv</h2>
      <table>
        <thead>
          <tr>
            <th>Column Name</th>
            <th>Data Type</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>city_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>city_name</td>
            <td>object</td>
          </tr>
        </tbody>
      </table>
    </td>
    <td>
      <h2>store_names.csv</h2>
      <table>
        <thead>
          <tr>
            <th>Column Name</th>
            <th>Data Type</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>store_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>store_name</td>
            <td>object</td>
          </tr>
        </tbody>
      </table>
    </td>
    <td>
      <h2>product_names.csv</h2>
      <table>
        <thead>
          <tr>
            <th>Column Name</th>
            <th>Data Type</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>product_id</td>
            <td>object</td>
          </tr>
          <tr>
            <td>product_name</td>
            <td>object</td>
          </tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>

## Initial Observations on Data Significance

### First 5 Rows of Each Dataset & Column Descriptions
### sales.csv
This csv file provides insights into product sales, revenue, stock levels, pricing, and promotional effectiveness across different stores and dates.

| product_id | store_id | date       | sales | revenue | stock | price | promo_type_1 | promo_bin_1 | promo_type_2 | promo_bin_2 | promo_discount_2 | promo_discount_type_2 |
|------------|----------|------------|-------|---------|-------|-------|--------------|-------------|--------------|-------------|-----------------|----------------------|
| P0001      | S0002    | 02/01/17   | 0.0   | 0.00    | 8.0   | 6.25  | PR14         | NaN         | PR03         | NaN         | NaN             | NaN                  |
| P0001      | S0012    | 02/01/17   | 1.0   | 5.30    | 0.0   | 6.25  | PR14         | NaN         | PR03         | NaN         | NaN             | NaN                  |
| P0001      | S0013    | 02/01/17   | 2.0   | 10.59   | 0.0   | 6.25  | PR14         | NaN         | PR03         | NaN         | NaN             | NaN                  |
| P0001      | S0023    | 02/01/17   | 0.0   | 0.00    | 6.0   | 6.25  | PR14         | NaN         | PR03         | NaN         | NaN             | NaN                  |
| P0001      | S0025    | 02/01/17   | 0.0   | 0.00    | 1.0   | 6.25  | PR14         | NaN         | PR03         | NaN         | NaN             | NaN                  |

**Column Descriptions**
*   `product_id` - The unique identifier of a product
*   `store_id` - The unique identifier of a store
*   `date` - Sales date (YYYY-MM-DD)
*   `sales` - Sales quantity
*   `revenue` - Daily total sales revenue
*   `stock` - End of day stock quantity
*   `price` - Product sales price
*   `promo_type_1` - Type of promotion applied on channel 1
*   `promo_bin_1` - Binned promotion rate for applied promo_type_1
*   `promo_type_2` - Type of promotion applied on channel 2
*   `promo_bin_2` - Binned promotion rate for applied promo_type_2
*   `promo_discount_2` - Discount rate for applied promo type 2
*   `promo_discount_type_2` - Type of discount applied

### product_hierarchy.csv
This csv file provides details about product dimensions such as length, depth, and width, along with cluster and hierarchy IDs.

| product_id | product_length | product_depth | product_width | cluster_id | hierarchy1_id | hierarchy2_id | hierarchy3_id | hierarchy4_id | hierarchy5_id |
|------------|----------------|---------------|---------------|------------|---------------|---------------|---------------|---------------|---------------|
| P0000      | 5.0            | 20.0          | 12.0          | NaN        | H00           | H0004         | H000401       | H00040105     | H0004010534   |
| P0001      | 13.5           | 22.0          | 20.0          | cluster_5  | H01           | H0105         | H010501       | H01050100     | H0105010006   |
| P0002      | 22.0           | 40.0          | 22.0          | cluster_0  | H03           | H0315         | H031508       | H03150800     | H0315080028   |
| P0004      | 2.0            | 13.0          | 4.0           | cluster_3  | H03           | H0314         | H031405       | H03140500     | H0314050003   |
| P0005      | 16.0           | 30.0          | 16.0          | cluster_9  | H03           | H0312         | H031211       | H03121109     | H0312110917   |

**Column Descriptions**
*   `product_id` - The unique identifier of a product
*   `product_length` - Length of product
*   `product_depth` - Depth of product
*   `product_width` - Width of the product
*   `Cluster_id` - Broader category of products
*   `hierarchy1_id` - Highest level of product classification
*   `hierarchy2_id` - Subcategory
*   `hierarchy3_id` - Sub-subcategory
*   `hierarchy4_id` - More specific sub-subcategory
*   `hierarchy5_id` - Most specific level

**Hierarchy Breakdown**

| Hierarchy Level | ID Example | Explanation (with Example)                                                                                                                                                                                                                                                                                                       |
|-----------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Root Category   | H00        | The most general classification.  Think of it as the broadest category. (e.g., Electronics)                                                                                                                                                                                                                                              |
| Subcategory 1   | H0004      | A more specific category within the Root. The "04" refines the classification. (e.g., within Electronics, this could be Audio Devices)                                                                                                                                                                                                  |
| Subcategory 2   | H000401    | A further refinement of Subcategory 1. The "01" adds another level of specificity. (e.g., within Audio Devices, this could be Headphones)                                                                                                                                                                                               |
| Subcategory 3   | H00040105  | Yet another level of detail. The "05" makes the category even more specific. (e.g., within Headphones, this could be Wireless Headphones)                                                                                                                                                                                          |
| Subcategory 4   | H0004010534| The most specific level shown in this example. The "34" likely represents a very specific product variation. (e.g., a specific model number or color of Wireless Headphones)                                                                                                                                                          |

**Key Principles Demonstrated in the Table:**

* **Hierarchical Structure:** Each row is a subcategory of the row above it.
* **Prefix Consistency:** Each ID starts with the ID of its parent category.
* **Suffix Addition:**  New characters are added to the end of the parent ID to create a more specific subcategory.
* **Context Dependence:** The actual meaning of the codes (H00, 04, 01, etc.) is arbitrary and requires a data dictionary. The examples provided are illustrative and may not reflect the true meaning of these codes in the real dataset.

### store_cities.csv
This csv file contains information about store identifiers, types, sizes, and the corresponding city identifiers.

| store_id | storetype_id | store_size | city_id |
|----------|--------------|------------|---------|
| S0091    | ST04         | 19         | C013    |
| S0012    | ST04         | 28         | C005    |
| S0045    | ST04         | 17         | C008    |
| S0032    | ST03         | 14         | C019    |
| S0027    | ST04         | 24         | C022    |

**Column Description**
*   `store_id` - The unique identifier of a store
*   `storetype_id`- Contains a list of store types that could mean "Supermarket" type and each number could represent specific type of supermarkets such as "Convenient Stores".
*   `store_size` - The size is not specified but would represent the square footage/meters.
*   `city_id` - The unique identifier of the city

### city_names.csv
This file maps city identifiers to their names, enabling geographical analysis and insights based on city-level data.

| city_id | city_name  |
|---------|------------|
| C001    | Amsterdam  |
| C002    | Berlin     |
| C003    | Barcelona  |
| C004    | Budapest   |
| C005    | Copenhagen |

### store_names.csv
This file associates store identifiers with their respective names, allowing for better identification and analysis of stores.

| store_id | store_name                 |
|----------|----------------------------|
| S0005    | MediaMarkt(National  Chain) |
| S0036    | Saturn                     |
| S0104    | Euronics                   |
| S0068    | FNAC                       |
| S0086    | Darty                      |

### product_names.csv
This file links product identifiers with their corresponding names, providing a mapping for easier reference and analysis.

| product_id | product_name             |
|------------|--------------------------|
| P0000      | Bottom Freezer Refrigerator |
| P0001      | Side-by-Side Refrigerator   |
| P0002      | Mini Fridge               |
| P0004      | Beverage Center           |
| P0005      | Wine Cooler               |

# Missing Values

## Identifying Missing Values
### Results
| Column Name | Missing Values | Column Name | Missing Values | Column Name | Missing Values |
|---|---|---|---|---|---|
| **sales.csv** |  | **product_hierarchy.csv** |  | **store_cities.csv** |  |
| product_id | 0 | product_id | 0 | store_id | 0 |
| store_id | 0 | product_length | 18 | storetype_id | 0 |
| date | 0 | product_depth | 16 | store_size | 0 |
| sales | 0 | product_width | 16 | city_id | 0 |
| revenue | 0 | cluster_id | 50 |  |  |
| stock | 0 | hierarchy1_id | 0 |  |  |
| price | 710 | hierarchy2_id | 0 |  |  |
| promo_type_1 | 0 | hierarchy3_id | 0 |  |  |
| promo_bin_1 | 43477 | hierarchy4_id | 0 |  |  |
| promo_type_2 | 0 | hierarchy5_id | 0 |  |  |
| promo_bin_2 | 49999 |  |  |  |  |
| promo_discount_2 | 49999 |  |  |  |  |
| promo_discount_type_2 | 49999 |  |  |  |  |

 -

| Column Name | Missing Values | Column Name | Missing Values | Column Name | Missing Values |
|---|---|---|---|---|---|
| **city_names.csv** |  | **store_names.csv** |  | **product_names.csv** |  |
| city_id | 107 | store_id | 0 | product_id | 0 |
| city_name | 107 | store_name | 0 | product_name | 0 |
|  |  |  |  |  |  |

## Addressing Missing Values
### Actions to be performed for missing values

| Column | Action | Section |
|---|---|---|
| price | Remove missing values | 1.1 |
| promo_bin_1 | Leave alone |  |
| promo_bin_2 | Leave alone |  |
| promo_discount_2 | Leave alone |  |
| promo_discount_type_2 | Leave alone |  |
| product_length | Fill out with similar values (Redacted - Removal)| 1.2 |
| product_depth | Fill out with similar values (Redacted - Removal) | 1.2 |
| product_width | Fill out with similar values (Redacted - Removal) | 1.2 |
| cluster_id | Fill out based on similar values (Redacted - Removal) | 1.3 |
| city_id | Remove missing values| 1.4
| city_name | Remove missing values | 1.4

#### Action 1.2
1. Created new df with the columns that have missing values
2. Checked the number of unique combinations of hierarchy IDs
    - The purpose behind checking the IDs is to apply logic to infer missing product dimensions.
    - There are 373 unique combinations
3. Checked how many products each have unique hierarchy ID combination has.
    - There are well over 200 unique ids for singular products.
4. Checked for any duplicates in the levels
    - There are duplicates at all levels

This indicates that hierarchy IDs are no longer reliable for filling in missing product dimensions.

**Conclusion:** Delete these rows instead.

#### Action 1.3

1. Investigated if there is a strong relationship between cluster_id and the hierarchal categories by creating visuals.
    - The visuals show a significantly dominant bar for hierarchy1_id, displaying an association but does not indicate strength in relationship.
2. Applied Contingency Tables, Chi-Squared Test, and Cramér's V (for all subcategories):

| Metric                 | hierarchy1_id | hierarchy2_id | hierarchy3_id | hierarchy4_id | hierarchy5_id | Conclusions |
|------------------------|---------------|---------------|---------------|---------------|---------------|-------------|
| Chi-Squared Statistic | 3547.594045   | 3547.594045   | 3547.594045   | 3547.594045   | 3547.594045   |      Delete the rows       |
| P-value              | 0.000065      | 0.000065      | 0.000065      | 0.000065      | 0.000065      |      Delete the rows       |
| Cramér's V           | 0.232594      | 0.232594      | 0.232594      | 0.232594      | 0.232594      |      Delete the rows       |

   - The results above indicate that all IDs statistically *generally* suggest a stronger relationship. The p values across all IDs suggest all IDs are statistically significant. Cramer's suggest all IDs have a weak to moderate association.  
**Conclusion:** Remove these rows instead

# Formatting Data

## Finding Duplicates

### Results
After searching all 6 csv's, There does not exist any duplicate rows. Perhaps in the previous cleaning procedures, duplicates might have been removed unintentionally.  

| File Name                                  | Total Rows | Duplicate Rows |
|--------------------------------------------|------------|---------------|
| city_names_1_numbers_cleaned.csv           | 37         | 0             |
| product_hierarchy_1_numbers_cleaned.csv    | 633        | 0             |
| sales_1_date_formatted_numbers_cleaned.csv | 49,289     | 0             |
| product_names.csv                          | 699        | 0             |
| store_cities.csv                           | 144        | 0             |
| store_names.csv                            | 144        | 0             |

# Standardizing Text

### Results

Leading/Trailing Spaces exist in 3 spreadsheets - in which one of them have multiple spaces.

**product_names.csv**

| File Name        | Column        | Leading/Trailing Spaces | Multiple Spaces |
|------------------|--------------|-------------------------|----------------|
| product_names.csv | product_name | 1                       | 0              |

**store_cities.csv**

| File Name       | Status               |
|-----------------|----------------------|
| store_cities.csv | ✅ No extra spaces found |

**store_names.csv**

| File Name       | Column      | Leading/Trailing Spaces | Multiple Spaces |
|-----------------|------------|-------------------------|----------------|
| store_names.csv | store_name | 4                       | 2              |

**city_names_1_numbers_cleaned.csv**

| File Name                        | Column    | Leading/Trailing Spaces | Multiple Spaces |
|----------------------------------|-----------|-------------------------|----------------|
| city_names_1_numbers_cleaned.csv | city_name | 9                       | 0              |


**product_hierarchy_1_numbers_cleaned.csv**

| File Name                          | Status               |
|------------------------------------|----------------------|
| product_hierarchy_1_numbers_cleaned.csv | ✅ No extra spaces found |

**sales_1_date_formatted_numbers_cleaned.csv**

| File Name                              | Status               |
|----------------------------------------|----------------------|
| sales_1_date_formatted_numbers_cleaned.csv | ✅ No extra spaces found |
