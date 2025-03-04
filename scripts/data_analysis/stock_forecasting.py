import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt


def load_data(filepath):
    """Loads daily stock data."""
    df = pd.read_csv(filepath, parse_dates=["date"])
    return df.groupby("date")["stock"].sum().reset_index().rename(columns={"date": "ds", "stock": "y"})


def train_stock_forecast(df):
    """Fits Prophet model to forecast inventory levels."""
    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return forecast


if __name__ == "__main__":
    stock_df = load_data("data/Sales.csv")
    stock_forecast = train_stock_forecast(stock_df)

    stock_forecast.to_csv("reports/stock_forecast_results.csv", index=False)
    print("✅ Stock Forecasting Completed! Results saved.")
