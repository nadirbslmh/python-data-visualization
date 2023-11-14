import seaborn as sns
import matplotlib.pyplot as plt

cars = sns.load_dataset("mpg")

sns.catplot(
    data=cars,
    kind="bar",
    x="cylinders",
    y="mpg",
    hue="origin",
)

plt.show()
