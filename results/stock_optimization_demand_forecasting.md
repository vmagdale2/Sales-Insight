# 📊 Stock Optimization & Demand Forecasting

## **📊 Business Problem**

Retailers must **balance stock levels** efficiently to **prevent overstocking or stockouts**. This project analyzes stock trends and forecasts demand to help businesses make **data-driven inventory decisions**.

## **🔍 Data Overview**

The dataset includes **sales, stock levels, and revenue data** for various stores and products:

- **Sales Data (********`sales_2_final.csv`********)**: Contains daily sales, stock availability, and pricing information.
- **Additional Attributes**: Includes product details, promotions, and store IDs.

## **📊 Methodology**

### **1️⃣ Data Preprocessing**

- Cleaned missing values and ensured data consistency.
- Converted `date` field to a proper datetime format.
- Aggregated stock and sales data for analysis.

### **2️⃣ Stock Level Analysis**

- **Created a heatmap** to visualize overstocked vs. understocked stores.
- **Compared stock levels** across different locations.

### **3️⃣ Sales vs. Stock Trends**

- Analyzed **sales trends over time** compared to stock levels.
- Identified patterns where **low stock may have impacted sales.**

### **4️⃣ Demand Forecasting (External - Python Model)**

- Built a **Prophet-based time series model** to predict future demand.
- Forecasting visualizations were generated and **uploaded as images to Tableau.**

## **📊 Key Insights**

### **🌟 Stock Level Heatmap Insights**

- **Several stores were consistently understocked**, leading to demand loss.
- **Some stores frequently ran out of stock**, missing revenue opportunities.

### **📈 Sales vs. Stock Trend Analysis**

- **Clear correlation** between stock availability and sales.
- **Stockouts coincided with lower sales performance.**

### **💡 Demand Forecasting Insights (Python)**

- **Forecasted seasonal trends** in sales to predict demand spikes.
- Recommended **optimal stock replenishment schedules.**
- Recommend to re-evaluate without aggregated at the monthly level data. Best to work with true daily variations if possible. 

## **👨‍💼 Business Impact**

- 🛍️ **Better Inventory Planning**: Reduce waste and prevent lost sales.
- 📈 **Data-Driven Stock Adjustments**: Ensure products are available when needed.
- 📉 **Strategic Store Restocking**: Prioritize high-demand stores for replenishment.

## **📈 Tableau Public Visualization**

🔗 **[View the Interactive Dashboard Here](https://public.tableau.com/app/profile/veronica.magdaleno/viz/Store_Segmentation_Results/optimization_forecast_dashboard)** *(To be updated with the published Tableau link!)*

## **🛠️ Tools Used**

- **Python** (`pandas`, `Prophet` for forecasting)
- **Tableau Public**
- **Google Colab**

## **🌐 Next Steps**

- **Incorporate real-time stock monitoring.**
- **Enhance forecasting with additional historical data.**
- **Develop automated stock replenishment models.**

