# Customer Segmentation (Clustering) Analysis

## 📋 Project Overview
This project aimed to segment stores based on sales performance, revenue generation, and product variety to identify distinct customer behavior patterns. By leveraging **K-Means Clustering**, we successfully identified meaningful segments that provide actionable insights for strategic decision-making.

---
## 📊 Dataset Information
- **Dataset Name:** `sales_2_final.csv`
- **Source:** Provided CSV file
- **Key Features Used:**
  - `sales` - Total sales per store
  - `revenue` - Total revenue per store
  - `unique_products` - Number of distinct products sold per store
  - `avg_transaction_value` - Average value of customer transactions
  - `sales_per_product` - Sales normalized by product variety

---
## 🔍 Key Insights
Based on the clustering results, the following insights were derived:

### **Cluster 0: Low Sales/Revenue with Limited Product Variety**
- **Characteristics:**
  - Generally low sales and revenue figures.
  - Limited variety in product offerings.
- **Recommendation:**
  - Focus on cross-selling strategies or bundling promotions to improve revenue.

### **Cluster 1: High-Performing Stores**
- **Characteristics:**
  - Strong revenue performance with consistent sales across multiple product lines.
  - Higher `avg_transaction_value` and `sales_per_product` values indicate strong consumer spending patterns.
- **Recommendation:**
  - Maintain current strategies and explore premium product expansions.

### **Cluster 2: Niche or Specialized Stores**
- **Characteristics:**
  - Sales may vary widely, but they specialize in specific product types with consistent customer interest.
  - Product mix management could be enhanced.
- **Recommendation:**
  - Introduce targeted marketing campaigns to maximize returns on niche products.

### **Cluster 3: Balanced Performance Stores**
- **Characteristics:**
  - Balanced sales, revenue, and product variety with moderate `avg_transaction_value`.
  - These stores may serve as valuable testing grounds for new product launches or pilot campaigns.
- **Recommendation:**
  - Experiment with localized promotions or seasonal strategies to boost performance.

---
## 📈 Visualizations
The following Tableau visualizations were created to enhance understanding of the results:

1. **Cluster Distribution Scatter Plot**
   - **X-axis:** `sales`
   - **Y-axis:** `revenue`
   - **Color by:** `Cluster`

2. **Average Transaction Value vs. Sales per Product**
   - Visualizing the relationship between spending patterns and product variety.

3. **Cluster Breakdown by Store Count**
   - Pie chart or bar chart showing store count distribution across clusters.

📌 **Tableau Public Link:** [View Dashboard](https://public.tableau.com/views/ClusterIdentification/cluster_dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---
## 🛠️ Technical Approach
### Step 1: Data Preparation
- Cleaned and processed sales data to ensure data integrity.
- Created new features including:
  - `unique_products` (count of distinct products sold per store)
  - `avg_transaction_value` (revenue / total sales)
  - `sales_per_product` (sales normalized by product variety)

### Step 2: Clustering with K-Means
- Applied the **Elbow Method** to identify the optimal number of clusters (K=4).
- Scaled the dataset using `StandardScaler` to ensure fair clustering results.

### Step 3: Analysis
- Evaluated each cluster’s performance by analyzing:
  - Sales
  - Revenue
  - Product variety
  - Average transaction value
  - Sales per product

---
## 💡 Future Enhancements
- Integrating geographical insights if location data becomes available.
- Exploring additional clustering techniques like DBSCAN or Hierarchical Clustering for improved segmentation.

---
## 📣 Final Thoughts
This project effectively identifies key store segments that drive business performance. The insights gained can inform marketing strategies, optimize product placement, and improve overall sales growth. By integrating these insights into business decisions, companies can maximize their revenue potential while addressing the unique needs of different customer groups.
