import seaborn as sns
import matplotlib.pyplot as plt

taxis = sns.load_dataset("taxis")

sns.displot(taxis["fare"], kde=True, bins=15)

plt.show()
