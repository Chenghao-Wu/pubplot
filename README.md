# pubplot

## Overview

**pubplot** is a Python package that streamlines the creation of publication-quality figures using matplotlib. It provides pre-configured settings and styles that conform to common publication standards, making it easier to create consistent, professional-looking plots.

## Features

- Pre-configured settings for APS (American Physical Society) style figures
- Easy-to-use line style generator for consistent plot formatting
- Support for publication-quality fonts and sizes
- Automatic legend formatting
- Built-in color palettes optimized for scientific figures

## Installation

Install pubplot directly from GitHub using pip:

```bash
git clone https://github.com/Chenghao-Wu/pubplot.git
cd pubplot
pip install .
```

## Example:

Please find an example on [Colab](https://colab.research.google.com/drive/1O-Ui8XFysaTrif0kZ42sIcuxb18jOrtE?usp=sharing)

## Usage

### Basic Example

Here's a simple example showing how to create a plot with multiple curves using pubplot:

```python
import numpy as np
import matplotlib.pyplot as plt
import pubplot.aps_parameter
from pubplot.linestyle import linestyle_generator

def my_plot(t):
    # Create figure and axis
    fig, ax = plt.subplots(1)
    
    # Get line style generator
    linestyles = linestyle_generator()
    
    # Plot multiple curves with different styles
    ax.plot(t, t, label='$t$', **next(linestyles))
    ax.plot(t, t**2, label='$t^2$', **next(linestyles))
    ax.plot(t, t**3, label='$t^3$', **next(linestyles))
    ax.plot(t, t**4, label='$t^4$', **next(linestyles))
    ax.plot(t, np.log(1+t), label='$\ln(1+t)$', **next(linestyles))
    ax.plot(t, t**(1./2), label='$t^{1/2}$', **next(linestyles))
    ax.plot(t, t**(1./3), label='$t^{1/3}$', **next(linestyles))

    # Set labels and legend
    ax.set_xlabel('$t$')
    ax.set_ylabel('$f(t)$')
    ax.legend(loc='best', ncol=2)
    
    # Adjust layout and save
    fig.tight_layout(pad=0.1)
    fig.savefig('pubplot-aps-line-markers')

# Generate data and create plot
t = np.arange(0, 1.0+0.05, 0.05)
my_plot(t)
plt.close('all')
```

### Key Components

1. **APS Parameters**
   ```python
   import pubplot.aps_parameter
   ```
   Imports pre-configured settings that match APS journal requirements.

2. **Line Style Generator**
   ```python
   from pubplot.linestyle import linestyle_generator
   linestyles = linestyle_generator()
   ```
   Creates an iterator that yields different line styles (color, marker, line type) for each curve.

3. **Plot Formatting**
   - Use `**next(linestyles)` to automatically apply the next style
   - LaTeX formatting in labels (e.g., `'$t^2$'`)
   - Automatic legend placement and formatting

## Advanced Usage

### Customizing Line Styles

You can customize the line style generator:

```python
from pubplot.linestyle import linestyle_generator

# Custom colors and markers
linestyles = linestyle_generator(colors=['red', 'blue', 'green'],
                               markers=['o', 's', '^'])
```

### Multiple Subplots

```python
import pubplot.aps_parameter
from pubplot.linestyle import linestyle_generator

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
linestyles = linestyle_generator()

# First subplot
ax1.plot(x, y1, label='Data 1', **next(linestyles))
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.legend()

# Second subplot
ax2.plot(x, y2, label='Data 2', **next(linestyles))
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.legend()

fig.tight_layout()
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

**pubplot** is inspired by **[mpltex](https://github.com/liuyxpp/mpltex)** and builds upon its concepts to provide an easy-to-use interface for creating publication-quality figures.

## References

1. [mpltex](https://github.com/liuyxpp/mpltex)
2. [palettable](https://github.com/jiffyclub/palettable)
3. [APS Figure Format Style Guidelines](https://www.psychologicalscience.org/publications/aps-figure-format-style-guidelines)
