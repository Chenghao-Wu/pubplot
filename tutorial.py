# -*- coding: utf-8 -*-
"""tutorial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O-Ui8XFysaTrif0kZ42sIcuxb18jOrtE

# Getting Started with pubplot

This tutorial demonstrates how to use pubplot to create publication-quality figures. We'll cover basic plotting, customizing line styles, and creating multi-panel figures.
"""

!git clone https://github.com/Chenghao-Wu/pubplot.git
!cd pubplot
!pip install .


import numpy as np
import matplotlib.pyplot as plt
import pubplot.aps_parameter
from pubplot.linestyle import linestyle_generator

"""## 1. Basic Line Plot

Let's start with a simple line plot showing different mathematical functions.
"""

# Generate data
x = np.linspace(0, 5, 100)

# Create figure
fig, ax = plt.subplots(1)
linestyles = linestyle_generator()

# Plot different functions
ax.plot(x, np.sin(x), label='sin(x)', **next(linestyles))
ax.plot(x, np.cos(x), label='cos(x)', **next(linestyles))

ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.legend()
fig.tight_layout()
plt.show()

"""## 2. Customizing Line Styles

You can customize the line styles by specifying colors, markers, and line styles.
"""

# Custom line styles
custom_linestyles = linestyle_generator(
    colors=['red', 'blue', 'green'],
    markers=['o', 's', '^'],
    lines=['-', '--', ':'])

fig, ax = plt.subplots(1)

x = np.linspace(0, 2, 20)
ax.plot(x, x**2, label='$x^2$', **next(custom_linestyles))
ax.plot(x, x**3, label='$x^3$', **next(custom_linestyles))
ax.plot(x, np.exp(x), label='$e^x$', **next(custom_linestyles))

ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.legend()
fig.tight_layout()
plt.show()

"""## 3. Multi-Panel Figure

Create a figure with multiple subplots using pubplot styling.
"""

# Generate data
t = np.linspace(0, 10, 100)
noise = np.random.normal(0, 0.1, len(t))

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
linestyles = linestyle_generator()

# First subplot: Damped oscillation
y1 = np.exp(-0.2*t) * np.sin(2*t)
ax1.plot(t, y1, label='Damped', **next(linestyles))
ax1.plot(t, y1 + noise, label='With noise', **next(linestyles))
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax1.legend()

# Second subplot: Different frequencies
ax2.plot(t, np.sin(t), label='$f_1$', **next(linestyles))
ax2.plot(t, np.sin(2*t), label='$f_2$', **next(linestyles))
ax2.plot(t, np.sin(3*t), label='$f_3$', **next(linestyles))
ax2.set_xlabel('Time')
ax2.set_ylabel('Amplitude')
ax2.legend()

fig.tight_layout()
plt.show()

"""## 4. Scatter Plot with Error Bars

Create a scatter plot with error bars using pubplot styling.
"""

# Generate data with errors
x = np.linspace(0, 10, 15)
y = 3 * np.exp(-0.3 * x) + 0.5
yerr = 0.2 * np.random.random(len(x))

fig, ax = plt.subplots(1)
linestyles = linestyle_generator()

# Plot data points with error bars
ax.errorbar(x, y, yerr=yerr, label='Experimental',
           capsize=3, **next(linestyles))

# Plot theoretical curve
x_fine = np.linspace(0, 10, 100)
y_theory = 3 * np.exp(-0.3 * x_fine) + 0.5
ax.plot(x_fine, y_theory, label='Theory', **next(linestyles))

ax.set_xlabel('Time (s)')
ax.set_ylabel('Signal (a.u.)')
ax.legend()
fig.tight_layout()
plt.show()

"""## 5. Saving Publication-Ready Figures

Demonstrate how to save figures in different formats suitable for publication.
"""

def create_sample_plot():
    fig, ax = plt.subplots(1)
    linestyles = linestyle_generator()

    x = np.linspace(0, 2*np.pi, 100)
    ax.plot(x, np.sin(x), label='sin(x)', **next(linestyles))
    ax.plot(x, np.cos(x), label='cos(x)', **next(linestyles))

    ax.set_xlabel('$x$')
    ax.set_ylabel('$f(x)$')
    ax.legend()
    fig.tight_layout()
    return fig

# Create and save figure in different formats
fig = create_sample_plot()

# Save as PDF (vector format, good for publications)
fig.savefig('example_plot.pdf', dpi=300, bbox_inches='tight')

# Save as PNG (raster format, good for web)
fig.savefig('example_plot.png', dpi=300, bbox_inches='tight')

plt.close()

