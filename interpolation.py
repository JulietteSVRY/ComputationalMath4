import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Define the function for which the data was obtained
def f(x):
    return np.sin(x)

# Generate sample data points
x = np.linspace(0, 2*np.pi, 10)
y = f(x)

# Perform cubic spline interpolation
cs = CubicSpline(x, y)

# Generate points for plotting the original function
x_fine = np.linspace(0, 2*np.pi, 100)
y_fine = f(x_fine)

# Generate points for plotting the interpolated function
x_interp = np.linspace(0, 2*np.pi, 100)
y_interp = cs(x_interp)

# Plot the original function, data points, and interpolated function
plt.plot(x_fine, y_fine, label='Original Function')
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_interp, y_interp, label='Interpolated Function')
plt.legend()
plt.show()
