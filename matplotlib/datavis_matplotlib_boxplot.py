import pandas as pd
import matplotlib.pyplot as plt
import os

dataset = os.environ["DATASET"]

df = pd.read_csv(f"{dataset}")
df.set_index("transaction_id")

transaction_date_result = df.groupby(["transaction_date"]).mean(numeric_only=True)

transaction_dates = transaction_date_result.index.get_level_values(0).tolist()
amount_averages = transaction_date_result["transaction_amount"]

plt.boxplot(amount_averages)
plt.show()
