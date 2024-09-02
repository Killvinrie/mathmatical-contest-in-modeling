import pandas as pd
import numpy as np

m = int(input("please enter the number of the candidates\n"))
n = int(input("please enter the number of the features\n"))

kind = input("please enter the correct order type of the features 1.max 2.min 3.mean 4.range").split(" ")
print(kind)

df = pd.read_excel("douban_top250.xlsx", "Sheet1", engine="openpyxl")

print(df.head(10))

print("please give the data matrix")

A = np.zeros(shape=(4, 4))
for i in range(2):
    A[i] = (input("please enter the /%st candidate").split(" "))
    A[i] = list(map(float, A[i]))
# A = [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]
# a = np.array(A)
# print(a)
# print(type(np.array(A)))
# b = list(a[:, 1])
# print(b, type(b))
# print(a[:, 1])


def min_max(X, i):
    max_val = max(X[:, i])
    ans = [(max_val - element) for element in X[:, i]]
    return np.array(ans)


def mid_max(X, i, mean):
    delta = [abs(element - mean) for element in X[:, i]]
    max = max(delta)
    if max == 0:
        max = 1
    ans = [(1 - e / max) for e in delta]
    return np.array(ans)


def range_max(X, high, low, i):
    x = list(X[:, i])
    m = max(x - min(x), max(x) - x)
    if m == 0:
        m = 1
    ans = []
    for i in range(len(x)):
        if x[i] < low:
            ans.append([1 - (low - x[i]) / m])
        elif x[i] > high:
            ans.append(1 - (x[i] - high) / m)
        else:
            ans.append(1)
    return np.array(ans)


X = np.zeros(shape=(4, 4))

for i in range(n):
    if kind[i] == 1:
        X.

