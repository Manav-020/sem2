import pandas as pd


asking_prices = pd.Series([15000, 18000, 20000, 17000, 22000])
fair_prices = pd.Series([16000, 17500, 21000, 18000, 22500])


good_deals = asking_prices[asking_prices < fair_prices].index.tolist()

print("Indices of good deals:", good_deals)


