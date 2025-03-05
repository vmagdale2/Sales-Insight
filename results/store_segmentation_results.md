# 📊 Store Performance Segmentation Analysis

## **📊 Business Problem**
Retail businesses need to **optimize store performance** by identifying **high, medium, and low-performing stores**. Understanding store segmentation helps in **inventory distribution, promotional strategies, and overall business growth**.

## **🔍 Data Overview**
The dataset includes store-level sales and revenue data:
- **Store Sales Data** (`store_sales.csv`): Contains store ID, total sales, and assigned cluster labels.
- **Cluster Statistics** (`cluster_stats.csv`): Provides aggregate statistics for each cluster.

## **📊 Methodology**
### **1️⃣ Data Preprocessing**
- Cleaned missing values and ensured data consistency.
- Standardized column formats for merging datasets.

### **2️⃣ Store Segmentation (K-Means Clustering)**
- Stores were segmented based on:
  - **Total Revenue**
  - **Sales Volume**
- K-Means Clustering was applied to identify **three store performance categories**:
  - **High Performance** (Cluster 2)
  - **Low Performance** (Cluster 0)
  - **Medium Performance** (Cluster 1)

## **📊 Key Insights**
### **🌟 High-Performance Stores (Cluster 2)**
- **Avg Sales:** `$98.24`
- **Total Stores:** `64`
- ✅ These stores are the most common but **have the lowest individual sales.**
- ✅ Likely **smaller stores or niche-market locations.**

### **🛠️ Low-Performance Stores (Cluster 0)**
- **Avg Sales:** `$290.16`
- **Total Stores:** `37`
- ✅ Moderate sales but **not the top-performing stores.**
- ✅ Can benefit from **targeted marketing & operational improvements.**

### **📈 Medium-Performance Stores (Cluster 1)**
- **Avg Sales:** `$979.39`
- **Total Stores:** `6`
- ✅ Highest sales per store but **few in number.**
- ✅ Likely **high-traffic flagship locations or premium stores.**

## **👨‍💼 Business Impact**
- 🛍️ **Better Inventory Planning**: High-performing stores may need **more stock** while low performers require **sales strategies.**
- 📈 **Optimized Marketing Efforts**: Low-performing stores can be **targeted for promotions** to boost performance.
- 💎 **Expansion Strategy**: Understanding what makes **medium-performance stores successful** can inform **future store planning.**

## **📈 Tableau Public Visualization**
🔗 **[Link to Interactive Dashboard](https://public.tableau.com/views/Store_Segmentation_Results/Dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)** 

## **🛠️ Tools Used**
- **Python** (`pandas`, `sklearn`)
- **K-Means Clustering**
- **Tableau Public**
- **Google Colab**

## **🌐 Next Steps**
- **Enhance segmentation analysis** with additional store attributes (size, region, etc.).
- **Develop targeted store-level strategies** to improve low-performing locations.
- **Incorporate trend analysis** to predict future store performance.

