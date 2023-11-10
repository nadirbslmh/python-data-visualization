import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"/home/nadir/codes/python-data-visualization/coffee_shop.csv")
df.set_index("transaction_id")

transaction_date_result = df.groupby(["transaction_date"]).mean(numeric_only=True)

transaction_dates = transaction_date_result.index.get_level_values(0).tolist()
amount_averages = transaction_date_result["transaction_amount"]

plt.figure(figsize=(15, 7))

plt.title("Transaction Amount Averages")
plt.xlabel("Transaction Dates")
plt.ylabel("Averages")

plt.plot(transaction_dates, amount_averages)

plt.show()
