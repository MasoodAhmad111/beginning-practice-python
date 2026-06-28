import numpy as np
import matplotlib.pyplot as plt

def quad(x, c):
    return c * x * (1 - x)

c_values = np.linspace(3.0, 4.0, 400)  
N_total = 1200
N_transient = 100
np.random.seed(1)
x = np.random.rand()
C_plot = []  #an empty list to store c values (parameter values)
X_plot = []  #an empty list to store x values (trajectory values)

for c in c_values:

    for n in range(N_total):
        x = quad(x, c)
        if n >= N_transient:
            C_plot.append(c) #adds the current parameter value c
            X_plot.append(x) #adds the current iterate value x
C_plot = np.array(C_plot)  #convert this Python list into a NumPy array for fast calculations and plotting.
X_plot = np.array(X_plot)

# plot
plt.figure()
plt.plot(C_plot, X_plot, ',')
plt.xlabel("c")
plt.ylabel("x")
plt.title("Bifurcation Diagram (Logistic Map)")
plt.show()
