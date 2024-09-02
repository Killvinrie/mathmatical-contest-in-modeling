import pandas as pd
import numpy as np

m = int(input("please enter the number of the candidates\n"))
n = int(input("please enter the number of the features\n"))

kind = input("please enter the correct order type of the features 1.max 2.min 3.mean 4.range").split(" ")
print(kind)


print("please give the data matrix")

A = np.zeros(shape=(4, 4))
for i in range(2):
    A[i] = (input("please enter the /%st candidate").split(" "))
    A[i] = list(map(float, A[i]))
# A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
# a = np.array(A)
# print(type(A))
# print(A)
# print(a)
# print(type(np.array(A)))
# b = list(a[:, 1])
# print(b, type(b))
# print(a[:, 1])


def min_max(X):
    max_val = max(X)
    ans = [(max_val - element) for element in X[i]]
    return np.array(ans)


def mid_max(X, mean):
    delta = [abs(element - mean) for element in list(X)]
    max = max(delta)
    if max == 0:
        max = 1
    ans = [(1 - e / max) for e in delta]
    return np.array(ans)


def range_max(X, high, low):
    x = list(X)
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
verti = np.zeros(shape =(4,1))
for i in range(n):
    if kind[i] == 1:   #max
        verti = np.array(A[:,i])
    elif kind[i] == 2: #min
        verti = min_max(A[:,i])
    elif kind[i] == 3:  #mean
        mean = eval(input("please enter the mean value"))
        verti = mid_max(A[:,i],mean)
    elif kind[i] == 4:  #range
        ref = input("please enter the high reference and the low reference seperated with space" ).split(" ")
        high_ref = eval(ref[0]) # need to convert to num
        low_ref = eval(ref[1])  # need to convert to num
        verti = range_max(A[:,i],high_ref,low_ref)
    # else:
    #     raise undefined_erro
    if i ==0:
        X = verti.reshape(-1,1)
    else:
        X = np.hstack([X,verti.reshape(-1,1)])
    print(X)




