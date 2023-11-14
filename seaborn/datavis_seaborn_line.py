import seaborn as sns
import matplotlib.pyplot as plt

cars = sns.load_dataset("mpg")

sns.lineplot(x="model_year", y="mpg", hue="origin", data=cars)

plt.show()
