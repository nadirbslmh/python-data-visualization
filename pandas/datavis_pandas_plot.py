import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/nadir/codes/python-data-visualization/coffee_shop.csv")
df.set_index("transaction_id")

tx_by_date = df.groupby(["transaction_date"]).mean(numeric_only=True)[
    "transaction_amount"
]

tx_by_date.plot(kind="line")

plt.show()
