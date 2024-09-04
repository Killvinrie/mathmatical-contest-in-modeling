import pandas as pd
import numpy as np

df = pd.read_excel("Sample.xlsx")
n = df.shape[0] - 1
m = df.shape[1] - 1
print(n, m)

kind = [1, 2, 3, 4, 1]

matrix = df.iloc[:, 1:].values
print(type(matrix))
print(matrix)
print(matrix[:, 0])
line_1 = matrix[:, 0]
line_2 = matrix[:, 1]
X = np.zeros(shape=(n, m))
for i in range(m):
    print("i", i)
    vert = matrix[:, i]
    print(X)

    if i == 0:
        X = vert.reshape(-1, 1)
    else:
        X = np.hstack([X, vert.reshape(-1, 1)])
print(X)

print(type(X == matrix))
