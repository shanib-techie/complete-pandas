import numpy as np

# ===============================
# COMMON HEADER (for all outputs)
# ===============================
name = "BHAWESH JOSHI"
roll = "CSC-24-14"
print(f"Name: {name} | Roll No: {roll}")
print("-" * 50)

# ==================================================
# (a) Mean, Std Dev, Variance along second axis

# ==================================================
print("\n(a) Mean, Std Dev, Variance (Axis = 1)")

arr_a = np.random.randint(1, 100, size=(3, 4))
print("Array:\n", arr_a)

mean_a = np.mean(arr_a, axis=1)
std_a = np.std(arr_a, axis=1)
var_a = np.var(arr_a, axis=1)

print("Mean:", mean_a)
print("Standard Deviation:", std_a)
print("Variance:", var_a)

# ==================================================
# (b) Create m x n array and reshape to n x m
"""name = "bhawesh joshi"
roll = "CSC-24-14"
"""

# ==================================================
print(" \n(b) Create & Reshape Array")

m = int(input("Enter m: "))
n = int(input("Enter n: "))

arr_b = np.random.randint(1, 50, size=(m, n))
print("Original Array:\n", arr_b)
print("Shape:", arr_b.shape)
print("Type:", type(arr_b))
print("Data Type:", arr_b.dtype)

reshaped = arr_b.reshape(n, m)
print("Reshaped Array (n x m):\n", reshaped)

# ==================================================
# (c) Check zero, non-zero and NaN elements

"""name = "bhawesh joshi"
roll = "CSC-24-14"
"""
# ==================================================
print("\n(c) Zero, Non-zero and NaN elements")

arr_c = np.array([0, 5, np.nan, 8, 0, 3, np.nan])

zero_idx = np.where(arr_c == 0)
nonzero_idx = np.where(arr_c != 0)
nan_idx = np.where(np.isnan(arr_c))

print("Array:", arr_c)
print("Zero indices:", zero_idx)
print("Non-zero indices:", nonzero_idx)
print("NaN indices:", nan_idx)

# ==================================================
# (d) Covariance and Correlation
"""name = "bhawesh joshi"
roll = "CSC-24-14"
"""
# ==================================================
print("\n(d) Covariance & Correlation")

Array1 = np.random.randint(1, 20, 10)
Array2 = np.random.randint(1, 20, 10)
Array3 = np.random.randint(1, 20, 10)

Array4 = Array3 - Array2
Array5 = 2 * Array1

print("Array1:", Array1)
print("Array4:", Array4)
print("Array5:", Array5)

cov = np.cov(Array1, Array4)
corr = np.corrcoef(Array1, Array5)

print("Covariance Matrix:\n", cov)
print("Correlation Matrix:\n", corr)

# ==================================================
# (e) Sum of first half & Product of second half
"""name = "bhawesh joshi"
roll = "CSC-24-14"
"""
# ==================================================
print("\n(e) Sum & Product of Array Halves")

A1 = np.random.randint(1, 10, 10)
A2 = np.random.randint(1, 10, 10)

print("Array1:", A1)
print("Array2:", A2)

sum_first_half = A1[:5] + A2[:5]
product_second_half = A1[5:] * A2[5:]

print("Sum of first half:", sum_first_half)
print("Product of second half:", product_second_half)
