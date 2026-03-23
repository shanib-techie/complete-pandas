import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml


titanic = fetch_openml(name='titanic', version=1, as_frame=True)
df = titanic.frame

print(df.head())


# gender_survival = df.groupby(['sex', 'survived']).size().unstack()

# gender_survival.plot(kind='bar')

# plt.title('Survival Count by Gender\nName: Shanib | Roll No: CSC/24/42')
# plt.xlabel('Gender')
# plt.ylabel('Number of Passengers')
# plt.legend(['Did Not Survive', 'Survived'])
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()



# plt.scatter(df['age'], df['fare'])

# plt.title('Scatter Plot of Age vs Fare\nName: Shanib | Roll No: CSC/24/42')
# plt.xlabel('Age')
# plt.ylabel('Fare')
# plt.tight_layout()
# plt.show()


# plt.figure()

# sns.kdeplot(df['age'].dropna(), label='Age', fill=True)
# sns.kdeplot(df['fare'].dropna(), label='Fare', fill=True)

# plt.title('Density Distribution of Age and Fare\nName: Shanib | Roll No: CSC/24/42')
# plt.xlabel('Value')
# plt.ylabel('Density')
# plt.legend()
# plt.tight_layout()
# plt.show()


sns.pairplot(df[['age', 'fare', 'pclass', 'survived']].dropna())
plt.suptitle('Pairwise Feature Distribution\nName: Shanib | Roll No: CSC/24/42', y=1.02)
plt.show()



