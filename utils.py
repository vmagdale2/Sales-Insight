import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from prophet import Prophet
from mlxtend.frequent_patterns import fpgrowth, association_rules
import logging

# ✅ Setup logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


### 📌 1️⃣ GOOGLE DRIVE SUPPORT ###
def mount_drive():
    """Mounts Google Drive for accessing CSV files."""
    from google.colab import drive
    drive.mount('/content/drive')
    print("✅ Google Drive Mounted. Use absolute paths for loading data.")


### 📌 2️⃣ FLEXIBLE FILE PATH HANDLING ###
def load_data(filepath, usecols=None, parse_dates=None):
    """Loads a dataset from CSV and handles missing file errors gracefully."""
    if not os.path.exists(filepath):
        logging.error(f"❌ ERROR: File not found - {filepath}")
        return pd.DataFrame()  # ✅ Return an empty DataFrame instead of None

    try:
        df = pd.read_csv(filepath, usecols=usecols, parse_dates=parse_dates)
        logging.info(f"✅ Successfully loaded {filepath}")
        return df
    except Exception as e:
        logging.error(f"❌ ERROR loading {filepath}: {e}")
        return pd.DataFrame()


def save_results(df, filepath):
    """Saves a DataFrame to CSV and handles errors."""
    try:
        df.to_csv(filepath, index=False)
        logging.info(f"✅ Results saved to {filepath}")
    except Exception as e:
        logging.error(f"❌ ERROR saving {filepath}: {e}")


### 📌 3️⃣ DATA VALIDATION ###
def check_missing_values(df):
    """Returns columns with missing values and their percentage."""
    missing = df.isnull().sum()
    missing_percentage = (missing / len(df)) * 100
    return missing_percentage[missing_percentage > 0]


def check_duplicates(df):
    """Returns the number of duplicate rows in a DataFrame."""
    return df.duplicated().sum()


### 📌 4️⃣ DATA PREPROCESSING ###
def preprocess_sales_data(df):
    """Handles missing values and ensures date column is in datetime format."""
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
    df.fillna(0, inplace=True)
    return df


def create_transaction_matrix(df):
    """Converts sales data into a Boolean matrix for Market Basket Analysis."""
    basket_df = df.pivot_table(index="store_id", columns="product_id", values="sales", aggfunc="sum").fillna(0)
    return basket_df > 0  # Convert to Boolean


### 📌 5️⃣ FEATURE ENGINEERING ###
def create_customer_features(df):
    """Creates aggregated customer-level features."""
    return df.groupby("store_id").agg({
        "sales": "sum",
        "revenue": "sum",
        "product_id": "nunique"
    }).reset_index().rename(columns={"product_id": "unique_products"})


def define_churn_labels(df, churn_days=90):
    """Defines churn labels based on inactivity threshold."""
    df["date"] = pd.to_datetime(df["date"])
    latest_date = df["date"].max()

    customer_data = df.groupby("store_id").agg({
        "date": "max",
        "sales": "sum",
        "revenue": "sum"
    }).reset_index()

    customer_data["days_since_last_purchase"] = (latest_date - customer_data["date"]).dt.days
    customer_data["churn"] = (customer_data["days_since_last_purchase"] > churn_days).astype(int)

    return customer_data.drop(columns=["date"])


### 📌 6️⃣ MACHINE LEARNING HELPERS ###
def train_random_forest(X, y):
    """Trains a Random Forest classifier and returns the trained model."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model, X_train, X_test, y_train, y_test


def scale_features(df):
    """Scales numerical features using StandardScaler."""
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df)
    return pd.DataFrame(scaled_features, columns=df.columns)


### 📌 7️⃣ MODEL EVALUATION ###
def evaluate_classification_model(model, X_test, y_test):
    """Evaluates a classification model using accuracy and classification report."""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    logging.info(f"Model Accuracy: {accuracy:.4f}")
    print(report)


def model_feature_importance(model, feature_names):
    """Returns feature importance for trained models."""
    return pd.DataFrame({"Feature": feature_names, "Importance": model.feature_importances_}).sort_values(
        by="Importance", ascending=False)


### 📌 8️⃣ TIME SERIES FORECASTING ###
def train_prophet_model(df, periods=30):
    """Trains a Prophet model and forecasts the next N days."""
    df = df.rename(columns={"date": "ds", "sales": "y"})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast


### 📌 9️⃣ ASSOCIATION RULE MINING ###
def run_fpgrowth(df, min_support=0.1):
    """Runs FP-Growth on a Boolean transaction matrix."""
    return fpgrowth(df, min_support=min_support, use_colnames=True)


def generate_association_rules(frequent_itemsets):
    """Generates association rules based on lift metric."""
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    return rules[rules["antecedents"].apply(lambda x: len(x) == 1) & rules["consequents"].apply(lambda x: len(x) == 1)]
