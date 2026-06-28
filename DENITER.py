import numpy as np
import matplotlib.pyplot as plt

def quad(x):
    return c * x * (1 - x)

c = 4
N = 20000
iterations = 5
x = np.random.rand(N)   

plt.figure(figsize=(10, 8))
for j in range(iterations):
    x = quad(x)
    plt.subplot(iterations, 1, j+1)
    plt.hist(x, bins=100, density=True, color='blue', alpha=0.7)
    plt.title(f"Iteration {j}")
    # iterate all points
    
plt.tight_layout()
plt.show()