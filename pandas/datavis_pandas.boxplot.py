import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/nadir/codes/python-data-visualization/coffee_shop.csv")
df.set_index("transaction_id")

amount_sums = df.groupby(["transaction_date"]).sum(numeric_only=True)[
    ["transaction_amount"]
]
amount_sums.boxplot()

plt.show()
