import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

x1 = np.linspace(0,1,10)
y1 = np.sin(x1)

# plt.plot(x,y)
# plt.title("y = sin(x)")
# plt.xlabel("x")
# plt.ylabel("y")
#
# plt.scatter(x, y, marker="1")
# plt.show()

fig , axes = plt.subplots(1,2)
axes[0].plot(x,y)
axes[1].scatter(x1 , y1 )
fig.show()

