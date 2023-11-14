import pandas as pd
import matplotlib.pyplot as plt
import os

dataset = os.environ["DATASET"]

df = pd.read_csv(f"{dataset}")
df.set_index("transaction_id")

amount_sums = df.groupby(["transaction_date"]).sum(numeric_only=True)[
    ["transaction_amount"]
]
amount_sums.boxplot()

plt.show()
