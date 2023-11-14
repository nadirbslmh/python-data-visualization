import seaborn as sns
import matplotlib.pyplot as plt

taxis = sns.load_dataset("taxis")

sns.pairplot(taxis.select_dtypes(["number"]))

plt.show()
