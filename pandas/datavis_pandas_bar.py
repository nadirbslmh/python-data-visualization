import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/nadir/codes/python-data-visualization/coffee_shop.csv")
df.set_index("transaction_id")

menu_freqs = df.groupby(["menu"]).count()["transaction_id"]
menu_freqs.plot(kind="bar", xlabel="Menu", ylabel="Frequencies", title="Ordered Menus")

plt.show()
