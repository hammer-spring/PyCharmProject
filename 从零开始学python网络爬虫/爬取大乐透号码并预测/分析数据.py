import os
import pandas as pd
import numpy as np

data = pd.read_csv(r'D:\PyCharm\PyCharmProject\从零开始学python网络爬虫\爬去大乐透号码并预测\data_recent.csv', sep=' ', header=None, error_bad_lines=False).values
data = data[:, 2:]

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 10))
ax = fig.gca(projection='3d')
a = np.random.randint(0, 5, size=100)
for i in range(1, 8):
    z = data[:100, i - 1]
    y = np.full_like(a, i)
    x = range(100)
    ax.plot(x, y, z)
ax.legend()
# ax.set_xlim=[0,8]
plt.tight_layout()
plt.savefig('img_3d.png')
plt.show()

