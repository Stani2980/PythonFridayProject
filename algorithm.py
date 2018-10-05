import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(100)
delta = np.random.uniform(-100, 200, size=(100,))
ys = .4 * x ** 2 + 3 + delta

plt.plot(x,ys)
plt.show()