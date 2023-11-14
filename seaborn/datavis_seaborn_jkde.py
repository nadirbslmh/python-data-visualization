import seaborn as sns
import matplotlib.pyplot as plt

taxis = sns.load_dataset("taxis")

sns.jointplot(x="tip", y="total", data=taxis, kind="kde", fill=True)

plt.show()
