import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"/home/nadir/codes/python-data-visualization/coffee_shop.csv")
df.set_index("transaction_id")

transaction_date_result = df.groupby(["transaction_date"]).mean(numeric_only=True)

transaction_dates = transaction_date_result.index.get_level_values(0).tolist()
amount_averages = transaction_date_result["transaction_amount"]

fig, axs = plt.subplots(2, 2, figsize=(30, 15))
fig.autofmt_xdate()

amount_sums = df.groupby(["transaction_date"]).sum(numeric_only=True)[
    "transaction_amount"
]
rating_averages = df.groupby(["transaction_date"]).mean(numeric_only=True)[
    "customer_rating"
]

axs[0, 0].plot(transaction_dates, amount_averages)
axs[0, 0].set_title("Transaction Amount Averages")

axs[0, 1].bar(transaction_dates, amount_averages)
axs[0, 1].set_title("Transaction Amount Averages per Date")

axs[1, 0].plot(transaction_dates, amount_sums)
axs[1, 0].set_title("Transaction Amount Total")

axs[1, 1].bar(transaction_dates, rating_averages)
axs[1, 1].set_title("Customer Rating Averages per Date")
axs[1, 1].set_xlabel("Rating")

fig.suptitle("Summary")

plt.show()
