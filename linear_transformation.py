import numpy as np
import matplotlib.pyplot as plt

# Transformation matrix
A = np.array([[2, 0],
              [0, 1]])

# Original basis vectors (x and y axes)
v1 = np.array([1, 0])
v2 = np.array([0, 1])

# Apply transformation: T(v) = A @ v
t_v1 = A @ v1
t_v2 = A @ v2

# Plot original and transformed basis
plt.figure(figsize=(6, 6))
plt.axhline(0, color='gray', lw=1)
plt.axvline(0, color='gray', lw=1)

# Original basis vectors (blue)
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original x-axis')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='cyan', label='Original y-axis')

# Transformed vectors (red)
plt.quiver(0, 0, t_v1[0], t_v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='Transformed x-axis')
plt.quiver(0, 0, t_v2[0], t_v2[1], angles='xy', scale_units='xy', scale=1, color='orange', label='Transformed y-axis')

plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.gca().set_aspect('equal')
plt.legend()
plt.title("Linear Transformation Example")
plt.show()
