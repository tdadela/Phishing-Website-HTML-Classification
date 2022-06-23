import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('data_training.csv')

print(df.info())
print(df.head())

sns.pairplot(df, hue='class')
plt.show()

corr = df.loc[:, df.columns != "class"].corr()

sns.set(style="darkgrid")

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, cmap=cmap, vmin=-1, vmax=1,
            square=True,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
plt.show()
