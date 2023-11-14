import seaborn as sns
import matplotlib.pyplot as plt

health_exps = sns.load_dataset("healthexp")

g = sns.relplot(
    x="Life_Expectancy",
    y="Spending_USD",
    hue="Country",
    alpha=0.5,
    palette="muted",
    height=6,
    data=health_exps,
)

g.set_xlabels(label="Life Expectancy")
g.set_ylabels(label="Spending in USD")

plt.show()
