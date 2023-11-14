import seaborn as sns
import matplotlib.pyplot as plt

taxis = sns.load_dataset("taxis")

sns.scatterplot(x="distance", y="total", data=taxis, hue="payment")

plt.show()
