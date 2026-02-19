import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris


# 
dict = {
    "name" : "shanib",
    "roll no ":"csc-24-42"
}
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.to_html("load_iris.html")
df['species'] = iris.target##
print("-"*50)

print(dict)
print(df.head())
print(df.describe())


mean = df.mean(numeric_only=True)##iss data me jaha numeric colun h sirf uska mean
# only sepal lenght
mane = df["sepal length (cm)"].mean()
# print("mean only of sepal lenght",mane)##just for practice
print(dict)
print("\nMean:\n", mean)


print("-"*50)
print(dict)
median = df.median(numeric_only=True)
print("\nMedian:\n", median)



print("-"*50)
print(dict)
mode = df.mode(numeric_only=True)
print("\nMode:\n", mode)


print("-"*50)
print(dict)
std = df.std(numeric_only=True)
print("\nStandard Deviation:\n", std)


print("-"*50)
print(dict)
se = std / np.sqrt(len(df))
print("\nStandard Error:\n", se)



ci_lower = mean - (1.96 * se)
ci_upper = mean + (1.96 * se)
print("-"*50)
print(dict)
print("\n95% Confidence Interval Lower:\n", ci_lower)
print("\n95% Confidence Interval Upper:\n", ci_upper)



# (b) Correlation Between Features + Heatmap
print("-"*50)
print(dict)
corr = df.corr(numeric_only=True)
print("\nCorrelation Matrix:\n", corr)
# # 🔸 Heatmap Plot
# plt.figure(figsize=(6,4))
# sns.heatmap(corr, annot=True)
# plt.title("Correlation Heatmap")
# plt.show()


# (c) Covariance between Sepal Length & Petal Length
print("-"*50)
# print(dict)
cov = np.cov(df['sepal length (cm)'], df['petal length (cm)'])
print("\nCovariance Matrix:\n", cov)


# (d) Contingency Table (Class Distribution)
print("-"*50)
# print(dict)
contingency = pd.crosstab(df['species'], columns="Count")
print("\nContingency Table:\n", contingency)
