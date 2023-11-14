import seaborn as sns
import matplotlib.pyplot as plt

taxis = sns.load_dataset("taxis")

sns.barplot(x="payment", y="total", data=taxis)

plt.show()
