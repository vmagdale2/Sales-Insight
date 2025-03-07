# 📊 Price Elasticity of Demand & Revenue Optimization

## **📊 Business Problem**
Effective pricing strategies are critical for maximizing revenue. This project analyzes **price elasticity** to understand how changes in price impact sales and revenue. By identifying which products are **elastic** (sensitive to price changes) or **inelastic** (stable demand despite price changes), businesses can make data-driven decisions for optimal pricing strategies.

## **🔍 Data Overview**
The dataset includes key variables for analyzing demand behavior:
- **`price`**: Product price across different stores and dates.  
- **`sales`**: Sales volume for each product-store combination.  
- **`revenue`**: Total revenue generated.  
- **Additional Fields**: Includes store identifiers, product details, and promotional data.

## **📊 Methodology**
### **1️⃣ Data Preprocessing**
- Cleaned missing values and ensured data consistency.  
- Aggregated data by product and date to identify sales patterns.  

### **2️⃣ Price vs. Sales Analysis**
- Built a **scatter plot** to identify relationships between price changes and sales.  
- Used **trend lines** to assess demand behavior across different price points.  

### **3️⃣ Price Elasticity Calculation**
- Developed a calculated field to compute **elasticity coefficients**:  
  ```sql
  (SUM([sales]) - LOOKUP(SUM([sales]), -1))
  /
  (SUM([price]) - LOOKUP(SUM([price]), -1))
  ```
- Visualized elasticity values using a **heatmap** to distinguish elastic vs. inelastic products.  

### **4️⃣ Revenue Trend Analysis**
- Created a **Revenue Trend Chart** to identify price-driven revenue shifts.  
- Used a **Moving Average Trendline** for smoother visual interpretation.  

## **📊 Key Insights**
### **🌟 Price vs. Sales Analysis**
- Several products displayed **high price elasticity**, where small price changes led to significant sales shifts.  
- Certain products showed **inelastic demand**, maintaining stable sales despite pricing adjustments.  

### **📈 Price Elasticity Heatmap**
- Products with high elasticity were identified as **prime candidates for promotions or discounts** to boost sales.  
- Inelastic products were highlighted as **ideal for price increases** to maximize revenue without major sales loss.  

### **📉 Revenue Trend Analysis**
- Revenue spikes aligned with **promotional price drops** for certain product categories.  
- Identified **price points** that maximize revenue without excessive discounts.  

## **👨‍💼 Business Impact**
- 💸 **Optimized Pricing Strategies**: Better understanding of elasticity helps create **targeted pricing campaigns**.  
- 🛍️ **Improved Inventory Planning**: Elasticity insights guide **promotion planning** and **stock adjustments**.  
- 📈 **Enhanced Revenue Forecasting**: Data-driven insights support **profit-maximizing strategies**.  

## **📈 Tableau Public Visualization**
🔗 **[View the Interactive Dashboard Here](https://public.tableau.com/app/profile/veronica.magdaleno/viz/Store_Segmentation_Results/elasticity_optimization_dashboard)** *(To be updated with the published Tableau link!)*

## **🛠️ Tools Used**
- **Python** (`pandas`, `numpy`) for data preparation and elasticity calculations.  
- **Tableau Public** for visualizing price-demand relationships.  
- **Google Colab** for data cleaning and advanced analytics.  

## **🌐 Next Steps**
- **Analyze cross-product elasticity effects** to identify product bundles for revenue growth.  
- **Incorporate competitor pricing data** for improved pricing decisions.  
- **Develop automated price recommendation models** for dynamic pricing strategies.

