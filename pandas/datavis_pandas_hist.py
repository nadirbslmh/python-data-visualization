import pandas as pd
import matplotlib.pyplot as plt
import os

dataset = os.environ["DATASET"]

df = pd.read_csv(f"{dataset}")
df.set_index("transaction_id")

tx_by_date = df.groupby(["transaction_date"]).mean(numeric_only=True)[
    "transaction_amount"
]

tx_by_date.hist(bins=20)

plt.show()
