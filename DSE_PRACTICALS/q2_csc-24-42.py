import pandas as pd
import numpy as np


list = {
    "name" : "ujjawal kumar sinha",
    "roll no " : "csc/24/55",
}
data = [
    [50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98],
    [45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93],
    [10, 12, 14, 16, 18, 1000, 22, 24, 26, 28, 30, 32, 34, 36, 38, -500, 42, 44, 46, 48, 50, 52, 54, 56, 58],
    [np.nan, 42, 44, 46, 48, 50, 52, 54, 56, 58, np.nan, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88],
    [45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93],
    [10, 12, 14, 16, 18, 1000, 22, 24, 26, 28, 30, 32, 34, 36, 38, -500, 42, 44, 46, 48, 50, 52, 54, 56, 58]
]
df = pd.DataFrame(data)
print(list)
print("Original DataFrame:")
print(df)
print("no. of row and columns in dataset")
print(df.shape)

# STEP 2️⃣: Missing values identify & count
print(list)
print("missing values :")
print(df.isnull().sum().sum())

# STEP 3️⃣: Data Cleaning
# (a) Drop duplicate rows
df_no_duplicates = df.drop_duplicates()
print(list)
print("\nAfter removing duplicate rows:")
print(df_no_duplicates)

# (b) Detect outliers using boxplot logic (IQR)
Q1 = df.drop_duplicates().quantile(0.25)
Q3 = df.drop_duplicates().quantile(0.75)
IQR = Q3 - Q1
outlier_mask = (df.drop_duplicates() < (Q1 - 1.5 * IQR)) | (df.drop_duplicates() > (Q3 + 1.5 * IQR))

outliers_per_row = outlier_mask.sum(axis=1)
print(list)
print("\nNumber of outliers per row:")
print(outliers_per_row)



df_cleaned = df.drop_duplicates()[outliers_per_row <= 2]

print("\nDataFrame after removing rows with >2 outliers:")
print(df_cleaned)




# STEP 4️⃣: Correlation analysis
corr_matrix = df_cleaned.corr()
print(list)
print("\nCorrelation Matrix:")
print(corr_matrix)

# Most positive & most negative correlated attributes
corr_pairs = corr_matrix.unstack()
corr_pairs = corr_pairs[corr_pairs.index.get_level_values(0) != corr_pairs.index.get_level_values(1)]

most_positive = corr_pairs.idxmax(), corr_pairs.max()
most_negative = corr_pairs.idxmin(), corr_pairs.min()
print(list)
print("\nMost Positively Correlated Attributes:")
print(most_positive)

print("\nMost Negatively Correlated Attributes:")
print(most_negative)