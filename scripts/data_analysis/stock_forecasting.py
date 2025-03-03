daily_sales = sales_df.groupby('date')['sales'].sum().reset_index()

from prophet import Prophet

daily_sales['ds'] = pd.to_datetime(daily_sales['date'])
daily_sales['y'] = daily_sales['sales']
daily_sales = daily_sales[['ds', 'y']]

model = Prophet()
model.fit(daily_sales)

future = model.make_future_dataframe(periods=30)  # Forecast 30 days into the future

forecast = model.predict(future)

fig1 = model.plot(forecast)

fig2 = model.plot_components(forecast)