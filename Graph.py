import numpy as np
import matplotlib.pyplot as plt

Y, X = np.mgrid[-10:10:0.1, -10:10:0.1]
U = X - X + 1
V = (X + Y) / (Y - X)

plt.figure(figsize=(10,10))
plt.streamplot(X, Y, U, V, density=3, color=U)

plt.show()