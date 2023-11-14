import pandas as pd
import matplotlib.pyplot as plt
import os

dataset = os.environ["DATASET"]

df = pd.read_csv(f"{dataset}")
df.set_index("transaction_id")

menu_count_result = df.groupby(["menu"]).count()

menu_counts = menu_count_result["transaction_id"]
menus = menu_count_result.index.get_level_values(0).tolist()

plt.pie(
    menu_counts,
    labels=menus,
    autopct="%.2f%%",
    startangle=90,
)

plt.show()
