import seaborn as sns
import matplotlib.pyplot as plt

taxis = sns.load_dataset("taxis")

sns.histplot(taxis["fare"], bins=15, kde=True)

plt.show()
