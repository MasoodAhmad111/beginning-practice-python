import numpy as np
import matplotlib.pyplot as plt

def quad(x, c_val):
    return c_val * x * (1 - x)

c_values = [3, 3.25, 3.5, 3.75, 4]
N = 50000
graph_number = 1
np.random.seed(1) 
initial_conditions = np.random.rand(2)  #creates 2 random initial conditions between 0 and 1.
for c in c_values:
    for x0 in initial_conditions:
        x = np.empty(N)   # Create an array of size N, but don’t fill it with any values yet.
        x[0] = x0
        for n in range(1,N):
           x[n] = quad(x[n-1], c)
        n = np.arange(N)
        plt.figure()
        plt.hist(x, bins=500, color='blue', density=True, edgecolor='black')
        plt.title(f"Graph {graph_number}, c = {c}, x0 = {x0:.10f}")
        graph_number += 1

plt.tight_layout()        
plt.show()
plt.close()