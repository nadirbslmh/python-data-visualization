import seaborn as sns
import matplotlib.pyplot as plt

taxis = sns.load_dataset("taxis")

sns.boxplot(x="pickup_borough", y="total", data=taxis, hue="payment")

plt.show()
