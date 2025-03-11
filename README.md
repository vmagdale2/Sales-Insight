# 📊 Sales-Insight: Unveiling Data-Driven Sales Strategies

## 📝 Project Description
To maintain its competitive edge, [Undisclosed Company] appointed me to conduct an in-depth sales analysis. The objective was to disclose actionable insights that would enhance sales strategies and operational efficiency.

---

## 🎯 Objectives
This project aimed to:
- Identify **high-performing stores** to optimize resource allocation.
- Forecast **future sales trends** for proactive stock control.
- Develop pricing strategies to maximize **revenue growth**.
- Discover frequently bought product pairs for **cross-selling strategies**.
- Segment stores and customers for **targeted marketing** and **engagement initiatives**.

---

## 📂 Dataset Overview
Due to confidentiality, the data is redacted. The dataset includes:
- **Sales Data:** Sales, revenue, stock, and promotional data.
- **Product Hierarchy:** Product dimensions, clusters, and hierarchy levels.
- **Store Attributes:** Store types, sizes, and locations.

For a detailed breakdown, refer to the **[Data README](data/README.md)**.

---

## 🧼 Data Cleaning Process
To ensure data integrity, the following cleaning steps were performed:
✅ **Missing Values:** Imputed or removed depending on the data context.  
✅ **Duplicates:** 49,289 duplicates were successfully removed.  
✅ **Inconsistent Formats:** Dates standardized to `YYYY-MM-DD`.  
✅ **Standardized Text:** Trimmed leading and trailing spaces for uniformity.  

**Processed datasets** are available in the [`data/processed`](data/processed) folder.  
**Interim datasets** for review are located in the [`data/interim`](data/interim) directory.  

For code details, see the **[Data Cleaning Notebook](notebooks/Data_Cleaning_Public.ipynb)**.

---

## 🔎 Exploratory Data Analysis (EDA)
Exploratory visualizations helped reveal critical insights about:
- Sales patterns
- Stock performance
- Customer purchasing behavior
- Revenue trends

---

## 📊 Analysis & Insights

### 🏬 **Store Performance Segmentation**
**Methodology:** Applied **K-Means Clustering** to segment stores based on revenue, sales, and product variety.

**Key Insights:**
- Identified **3 performance groups**: **High**, **Medium**, and **Low**.
- High-performing stores contributed over **60%** of total revenue.

🔗 [View Tableau Dashboard](https://public.tableau.com/views/SalesInsights1_17414714535380/store_segmentation_dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)  
📂 **[Store Segmentation Code](scripts/data_analysis/store_segmentation.py)**  

---

### 📉 **Stock Optimization & Demand Forecasting**
**Methodology:** Used **Prophet Forecasting** to predict demand trends and identify stock-out risks.

**Key Insights:**
- Forecasts revealed seasonal trends influencing stock levels.
- Recommended improved inventory replenishment strategies.

🔗 [View Tableau Dashboard](https://public.tableau.com/views/SalesInsights1_17414714535380/optimization_forecast_dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)  
📂 **[Stock Forecasting Code](scripts/data_analysis/stock_forecasting.py)**  

---

### 💰 **Price Elasticity of Demand & Revenue Optimization**
**Methodology:** Measured price elasticity to uncover optimal pricing strategies.

**Key Insights:**
- Products with high elasticity benefited from promotional pricing strategies.
- Adjusted price points to maximize revenue without reducing demand.

🔗 [View Tableau Dashboard](https://public.tableau.com/views/SalesInsights1_17414714535380/elasticity_optimization_dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)  
📂 **[Price Elasticity Code](scripts/data_analysis/elasticity_revenue_optimization.py)**  

---

### 🛒 **Market Basket Analysis (Association Rules)**
**Methodology:** Applied **FP-Growth** to identify frequently purchased item pairs.

**Key Insights:**
- Recommended cross-selling strategies to boost basket sizes.
- Used advanced metrics like **Lift**, **Jaccard**, and **Zhang’s Metric** to evaluate associations.

🔗 [View Tableau Dashboard](https://public.tableau.com/views/SalesInsights1_17414714535380/market_basket_dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)  
📂 **[Market Basket Analysis Code](scripts/data_analysis/market_basket_analysis.py)**  

---

### 🏷️ **Customer Segmentation (Clustering)**
**Methodology:** Applied **K-Means Clustering** to group stores based on sales patterns.

**Key Insights:**
- Identified 4 customer segments for tailored marketing campaigns.
- Recommended loyalty programs to improve retention.

🔗 [View Tableau Dashboard](https://public.tableau.com/views/ClusterIdentification/cluster_dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)  
📂 **[Customer Segmentation Code](scripts/data_analysis/customer_segmentation.py)**  

---

## 📋 Results Summary
**Key Business Insights:**
✅ Segmentation uncovered **top-performing stores**, improving resource allocation.  
✅ Forecasting helped mitigate **overstocking risks**.  
✅ Pricing adjustments improved **revenue growth**.  
✅ Market Basket Analysis revealed strategic **product pairings**.  
✅ Customer segmentation allowed for **targeted marketing campaigns**.  

---

## 📋 Project Deliverables
📄 **[Sales Insights Report](reports/Report.pdf)**  
📊 **[Sales Insights Presentation](reports/Sales_Insights_Presentation.pdf)**  
📈 **[Tableau Dashboard](https://github.com/vmagdale2/Sales-Insight)**

---

## 💻 How to Reproduce This Project
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/Sales-Insight.git
   cd Sales-Insight
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `.env` file:
   ```
   GOOGLE_DRIVE_PATH="/content/drive/My Drive/Education/Business Intelligence/Github Portfolio/"
   ```
4. Run the desired Python scripts:
   ```bash
   python scripts/store_segmentation.py
   python scripts/price_elasticity.py
   ```

---

## 🧰 Tools & Technologies Used
✅ **Python** for data analysis and machine learning  
✅ **Tableau Public** for interactive visualizations  
✅ **Prophet**, **FP-Growth**, **K-Means** for advanced analytics  
✅ **Google Colab** for efficient data manipulation  
✅ **GitHub** for version control and project organization  

---

## 📬 Contact Me
If you have any questions, feedback, or collaboration ideas, feel free to reach out:

📧 **Email:** [jobsearchvmagda@gmail.com](mailto:jobsearchvmagda@gmail.com)  
🔗 **[LinkedIn](https://www.linkedin.com/in/veronica-magdaleno-84248862/)**   

---

## 🚀 Final Words
This project was an incredible opportunity to apply my technical skills while honing my storytelling and visualization expertise. I'm excited to continue exploring data insights and delivering impactful results. 😊

