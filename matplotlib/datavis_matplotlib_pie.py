import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"/home/nadir/codes/python-data-visualization/coffee_shop.csv")
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
