#%%
# Import packages and dataset
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
sns.set_palette("colorblind")

tips = sns.load_dataset("tips")
tips.head()

#%%
# Scatterplot
sns.scatterplot(data=tips, x='total_bill', y='tip',hue='time',style='time', size='size')
plt.title("Scatter plot")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

#%%
# Line plot
sns.lineplot(data= tips, x = 'total_bill', y ='tip', hue='sex')
plt.title("Line Plot")
plt.show()

#%%
# Barplot, grouping by category and plotting the sums
sum_sex = tips.groupby('sex')['tip'].sum().reset_index()
sns.barplot(data=sum_sex, x='sex', y = 'tip')
plt.title("Bar Plot with sum of tip by sex")
plt.show()

#%%
# Boxplot
sns.boxplot(data=tips, x='sex', y='tip', hue = 'smoker')
plt.title("Box Plot of Total Bill by Day and Smoker Status")
plt.show()

#%%
# Pairs plot, combination of scatterplots & histograms
sns.pairplot(tips, hue="sex")
plt.title("Pair Plot of Iris Dataset")
plt.show()

#%%
# Histogram
sns.histplot(data=tips, x='tip', kde=True)
plt.title("Histogram of Total Tip")
plt.show()


#%%
# Multiple histograms
tips[["total_bill","tip","size"]].hist(bins=30, figsize=(15,10), layout=(4,2), sharex=False, sharey=False)