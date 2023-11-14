import seaborn as sns
import matplotlib.pyplot as plt

taxis = sns.load_dataset("taxis")
taxis_corr = taxis.corr(numeric_only=True)

sns.heatmap(taxis_corr, annot=True, cmap="coolwarm")

plt.show()
