import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt


def load_data(filepath):
    """Loads daily sales data."""
    df = pd.read_csv(filepath, parse_dates=["date"])
    return df.groupby("date")["sales"].sum().reset_index().rename(columns={"date": "ds", "sales": "y"})


def train_prophet_model(df):
    """Fits Prophet model and forecasts future sales."""
    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return forecast


if __name__ == "__main__":
    sales_df = load_data("data/Sales.csv")
    forecast_results = train_prophet_model(sales_df)

    forecast_results.to_csv("reports/retail_demand_forecast.csv", index=False)
    print("✅ Retail Demand Prediction Completed! Results saved.")
