import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from prophet import Prophet
from mlxtend.frequent_patterns import fpgrowth, association_rules


### 📌 1️⃣ DATA LOADING & SAVING ###
def load_data(filepath, usecols=None, parse_dates=None):
    """Loads a dataset from CSV, with optional column filtering & date parsing."""
    return pd.read_csv(filepath, usecols=usecols, parse_dates=parse_dates)

def save_results(df, filepath):
    """Saves a DataFrame to CSV."""
    df.to_csv(filepath, index=False)
    print(f"✅ Results saved to {filepath}")


### 📌 2️⃣ DATA PREPROCESSING ###
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


### 📌 3️⃣ MACHINE LEARNING HELPERS ###
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


### 📌 4️⃣ TIME SERIES FORECASTING ###
def train_prophet_model(df, periods=30):
    """Trains a Prophet model and forecasts the next N days."""
    df = df.rename(columns={"date": "ds", "sales": "y"})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast


### 📌 5️⃣ ASSOCIATION RULE MINING ###
def run_fpgrowth(df, min_support=0.1):
    """Runs FP-Growth on a Boolean transaction matrix."""
    return fpgrowth(df, min_support=min_support, use_colnames=True)

def generate_association_rules(frequent_itemsets):
    """Generates association rules based on lift metric."""
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    return rules[rules["antecedents"].apply(lambda x: len(x) == 1) & rules["consequents"].apply(lambda x: len(x) == 1)]
