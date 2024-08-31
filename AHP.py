import numpy as np

A = np.array([[1, 2, 3, 5], [1 / 2, 1, 1 / 2, 2], [1 / 3, 2, 1, 2], [1 / 5, 1 / 2, 1 / 2, 1]])
print(A)
n = A.shape[0]
print(n)

eig_val, eig_vec = np.linalg.eig(A)
print(eig_val, eig_vec)

max_eig = max(eig_val)

print(max_eig)

CI = (max_eig - n) / (n - 1)
Ri = [0.00, 0.00, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49]

CR = CI / Ri[n - 1]
print(CR)
if CR < 0.1:
    print("good")
else:
    print("bad")


A_sum = np.sum(A,axis=0)
print("a,sum",A_sum)
Stand_A = A/A_sum
A_sum_R = np.sum(Stand_A,axis=1)
print("A_SUM=",A_sum_R/4)
print("det=",np.linalg.det(A))