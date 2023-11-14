import pandas as pd
import matplotlib.pyplot as plt
import os

dataset = os.environ["DATASET"]

df = pd.read_csv(f"{dataset}")
df.set_index("transaction_id")

menu_freqs = df.groupby(["menu"]).count()["transaction_id"]
menu_freqs.plot(kind="bar", xlabel="Menu", ylabel="Frequencies", title="Ordered Menus")

plt.show()
