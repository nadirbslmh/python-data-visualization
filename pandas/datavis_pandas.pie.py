import pandas as pd
import matplotlib.pyplot as plt
import os

dataset = os.environ["DATASET"]

df = pd.read_csv(f"{dataset}")
df.set_index("transaction_id")

menu_freqs = df.groupby(["menu"]).count()["transaction_id"]
menu_freqs.plot.pie(y="menu", autopct="%.2f", figsize=(10, 6))

plt.show()
