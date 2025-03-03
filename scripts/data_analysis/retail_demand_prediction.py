# Rename columns for Prophet
sales_df = sales_df.rename(columns={"date": "ds", "sales": "y"})

# Train Prophet model
model = Prophet()
model.fit(sales_df)

# Create future predictions
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

fig = model.plot(forecast)
plt.savefig("reports/forecast_chart.png")
plt.show()