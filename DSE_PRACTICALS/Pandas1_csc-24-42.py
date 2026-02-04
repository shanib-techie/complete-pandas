import pandas as pd

print("Name: SHANIB | Roll No: CSC-24-42")

print("==============================================================\n")
# ==================================================
# (a) Create a Series with 5 elements and sort
# ==================================================
print("(a) Sorting Series by Index and Values")

s1 = pd.Series(
    [30, 10, 50, 20, 40],
    index=['c', 'a', 'e', 'b', 'd']
)

print("\nOriginal Series:")
print(s1)

print("\nSeries sorted by INDEX:")
# print(s1.sort_index())
print(s1.sort_index())

print("\nSeries sorted by VALUES:")
print(s1.sort_values())
# ==================================================
# (b) Series with duplicates & ranking
# ==================================================

print("\n(b) Ranking with 'first' and 'max' methods")

# Series jisme duplicate values hain
s2 = pd.Series([100, 200, 100, 300, 200, 100])

print("\nOriginal Series:")
print(s2)

# --------------------------------------------------
# method='first'
# --------------------------------------------------
# Agar duplicate value aayi,
# toh jo value PEHLE aayi hogi usko chhota rank milega
# aur baaki duplicates ko uske baad ke ranks milenge
rank_first = s2.rank(method='first')

# --------------------------------------------------
# method='max'
# --------------------------------------------------
# Agar duplicate value aayi,
# toh sabko SAME rank milega
# aur woh rank duplicates ke group ka MAX rank hota hai
rank_max = s2.rank(method='max')

print("\nRank using 'first' method:")
print(rank_first)

print("\nRank using 'max' method:")
print(rank_max)

# --------------------------------------------------
# Min aur Max rank nikalna (first method)
# --------------------------------------------------
print("\nMinimum & Maximum rank (first method):")
print("Min Rank:", rank_first.min())
print("Max Rank:", rank_first.max())

# --------------------------------------------------
# Min aur Max rank nikalna (max method)
# --------------------------------------------------
print("\nMinimum & Maximum rank (max method):")
print("Min Rank:", rank_max.min())
print("Max Rank:", rank_max.max())

# ==================================================
# (c) Index of minimum and maximum value
# ==================================================
print("\n(c) Index of Minimum and Maximum value")

s3 = pd.Series([45, 12, 78, 34, 90], index=['A', 'B', 'C', 'D', 'E'])

print("\nSeries:")
print(s3)

print("\nIndex of Minimum value:")
print(s3.idxmin())#sabse kam b ki val h 12 

print("\nIndex of Maximum value:")
print(s3.idxmax())
