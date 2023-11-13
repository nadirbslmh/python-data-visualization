import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/nadir/codes/python-data-visualization/coffee_shop.csv")
df.set_index("transaction_id")

menu_freqs = df.groupby(["menu"]).count()["transaction_id"]
menu_freqs.plot.pie(y="menu", autopct="%.2f", figsize=(10, 6))

plt.show()
