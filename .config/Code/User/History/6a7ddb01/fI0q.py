import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from control import place, ss, step_response, pzmap

# System matrices
A = np.array([[0, 1, 0],
              [0, 0, 1],
              [1, -5, -3]])
B = np.array([[0],
              [0],
              [1]])
C = np.array([[1, 0, 0]])
D = np.array([[0]])

# Desired poles
desired_poles = [-1 + 2j, -1 - 2j, -7]

# Place the poles
K = place(A, B, desired_poles)

# Closed-loop system
A_cl = A - np.dot(B, K)

# State-space representation of the closed-loop system
system_cl = ss(A_cl, B, C, D)

# Plot pole-zero diagram
plt.figure()
pzmap(system_cl, Plot=True, title='Pole-Zero Map')

# Step response
t, y = step_response(system_cl)

plt.figure()
plt.plot(t, y)
plt.title('Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.grid(True)

plt.show()
