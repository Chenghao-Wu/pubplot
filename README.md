# pubplot

## Overview

**pubplot** is used to streamline the figure plot process based on matplotlib.

## Installing
Downloading the source code from github and install it using pip.

```bash
$ git clone https://github.com/Chenghao-Wu/pubplot.git
$ cd pubplot
$ pip install .
```

## Usage

### Basic Example
```python
import pubplot.aps_parameter
from pubplot.linestyle import linestyle_generator

def my_plot(t):
    fig, ax = plt.subplots(1)
    linestyles = linestyle_generator()
    ax.plot(t, t, label='$t$', **next(linestyles))
    ax.plot(t, t**2, label='$t^2$', **next(linestyles))
    ax.plot(t, t**3, label='$t^3$', **next(linestyles))
    ax.plot(t, t**4, label='$t^4$', **next(linestyles))
    ax.plot(t, np.log(1+t), label='$\ln(1+t)$', **next(linestyles))
    ax.plot(t, t**(1./2), label='$t^{1/2}$', **next(linestyles))
    ax.plot(t, t**(1./3), label='$t^{1/3}$', **next(linestyles))

    ax.set_xlabel('$t$')
    ax.set_ylabel('$f(t)$')
    ax.legend(loc='best', ncol=2)
    fig.tight_layout(pad=0.1)
    fig.savefig('pubplot-aps-line-markers')

t = np.arange(0, 1.0+0.05, 0.05)
my_plot(t)
plt.close('all')
```

## Acknowledge
**pubplot** is a python package inspired by **[mpltex](https://github.com/liuyxpp/mpltex)**.

## Reference
1. https://github.com/liuyxpp/mpltex
2. https://github.com/jiffyclub/palettable
3. https://www.psychologicalscience.org/publications/aps-figure-format-style-guidelines

