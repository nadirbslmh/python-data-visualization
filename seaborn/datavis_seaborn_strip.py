import seaborn as sns
import matplotlib.pyplot as plt

taxis = sns.load_dataset("taxis")

sns.stripplot(x="pickup_borough", y="total", data=taxis, hue="payment", dodge=True)

plt.show()
