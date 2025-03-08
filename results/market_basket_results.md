# 📊 Market Basket Analysis (Association Rules)

## **📊 Business Problem**

Retailers need insights into **customer purchasing behavior** to improve product placement, drive cross-selling strategies, and create more effective promotions. This project leverages **Market Basket Analysis** to uncover product combinations frequently purchased together, revealing actionable insights for boosting sales.

## **🔍 Data Overview**

The dataset includes:

- **`antecedents`**: The initial product in the rule (e.g., "Product A").
- **`consequents`**: The product frequently purchased alongside the antecedent (e.g., "Product B").
- **`support`**: The proportion of transactions containing both items.
- **`confidence`**: The probability that if a customer buys `antecedent`, they will also buy `consequent`.
- **`lift`**: Measures the strength of the association rule; values >1 indicate a strong relationship.
- **`leverage`** & **`conviction`**: Provide additional insights into product dependency.
- **`jaccard`**, **`kulczynski`**, & **`zhang's metric`**: Advanced metrics for deeper insight into association rules.

## **📊 Methodology**

### **1️⃣ Data Preparation**

- Cleaned missing values and ensured data consistency.
- Modified column data for easier relationship identification.
- Filtered rules with meaningful support and confidence values to avoid weak associations. Restricted to the top 15 product associations.

### **2️⃣ Visualizing Insights**

- **Association Rules Network Graph** → Highlights product pairs with strong relationships.
- **Support vs. Confidence Scatter Plot** → Identifies reliable product pairs.
- **Metrics Table** → Displays detailed insights with key metrics such as `lift`, `leverage`, and `conviction`.

### **3️⃣ Interactive Filters**

- Added dynamic filters for:
  - **Support Threshold** → Focus on highly common product pairs.
  - **Confidence Threshold** → Identify the most reliable rules.
  - **Product Filters** → Allows deep dives into specific product combinations.

## **📊 Key Insights**

### **🌟 Association Rules Network Graph**

- Certain products consistently appeared together, revealing ideal opportunities for product bundling strategies.
- Some unexpected product pairings highlighted **cross-selling opportunities**.

### **📈 Support vs. Confidence Scatter Plot**

- Product pairs with **high support** and **high confidence** were identified as key drivers for increasing basket size.
- Items with low support but high lift were identified as **niche cross-sell opportunities**.

### **📊 Metrics Table Insights**

- Identified high `lift` product pairs ideal for **promotions** and **strategic placement**.
- Products with strong `conviction` values were seen as **reliable upsell candidates**.

### **💡 Advanced Metrics Insights**

- **`Jaccard`**\*\* values\*\* identified closely linked product pairs ideal for **aisle planning and co-marketing strategies**.
- **`Kulczynski`**\*\* values\*\* revealed products that are **mutually dependable** during promotions.
- **`Zhang’s Metric`** helped identify **hidden but strong product pairings** with high reliability.

## **👨‍💼 Business Impact**

- 🚀 **Improved Sales Through Bundling**: Products frequently purchased together were flagged for in-store promotions or online recommendations.
- 🛎️ **Enhanced Store Layout Optimization**: Strategic product placement improved customer convenience.
- 💳 **Increased Cross-Selling Opportunities**: Marketing teams can now focus on product pairs that maximize cart value.

## **📈 Tableau Public Visualization**

🔗 **[View the Interactive Dashboard Here](https://public.tableau.com/views/Store_Segmentation_Results/market_basket_dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)** *(To be updated with the published Tableau link!)*

## **🛠️ Tools Used**

- **Python** (`mlxtend`, `pandas`) for rule generation and data preparation.
- **Tableau Public** for interactive visualization.
- **Google Colab** for efficient data processing and analysis.

## **🌐 Next Steps**

- **Refine rules by incorporating additional customer segmentation data.**
- **Explore time-based trends to identify seasonal purchasing patterns.**
- **Develop product bundle recommendations for marketing campaigns.**

