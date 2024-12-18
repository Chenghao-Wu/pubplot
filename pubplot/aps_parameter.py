import matplotlib.pyplot as plt

import logging 
logging.getLogger('matplotlib.font_manager').disabled = True

from cycler import cycler
from palettable.colorbrewer.qualitative import Set1_9
from palettable.tableau import Tableau_10, Tableau_20
from palettable import cubehelix

almost_black = '#262626'

brewer_set1 = Set1_9.mpl_colors
# Remove the sixth color (yellow) which is too bright
brewer_set1.pop(5)
# Swap the red and blue to let blue come first
brewer_set1[0], brewer_set1[1] = brewer_set1[1], brewer_set1[0]
# Add a decent black color to this list
brewer_set1.append(almost_black)

default_color_cycler = cycler('color', brewer_set1)

width_single_column = 3.375
width_double_column = 6.75

GOLDEN_RATIO = 0.618
# Default ratio for a single plot figure
height_width_ratio = GOLDEN_RATIO * 1.1  # = height / width

_width = width_single_column
_height = width_single_column * height_width_ratio

_params = {'font.family': 'sans-serif',
        'font.serif': ['Times', 'Computer Modern Roman'],
        'font.sans-serif': ['Helvetica', 'Computer Modern Sans serif'],
        'font.size': 8,
        'pgf.rcfonts': False,
        'text.usetex': False,
        # To force LaTeX use Helvetica fonts.
        #'text.latex.preamble': [r'\usepackage{siunitx}',
        #                        r'\sisetup{detect-all}',
        #                        r'\usepackage{helvet}',
        #                        r'\usepackage[eulergreek,EULERGREEK]{sansmath}',
        #                        r'\sansmath'],
        #'text.latex.unicode': False,
        'axes.prop_cycle': default_color_cycler,
        'axes.labelsize': 8,
        'axes.linewidth': 1,
        'axes.unicode_minus': False,

        'figure.figsize': (_width, _height),
        # 'figure.subplot.left' : 0.125,
        # 'figure.subplot.right' : 0.95,
        # 'figure.subplot.bottom' : 0.1,
        # 'figure.subplot.top' : 0.95,

        'savefig.dpi': 300,
        'savefig.format': 'png',
        # 'savefig.bbox': 'tight',
        # this will crop white spaces around images that will make
        # width/height no longer the same as the specified one.

        'legend.fontsize': 7.5,
        'legend.frameon': False,
        'legend.numpoints': 1,
        'legend.handlelength': 2,
        'legend.scatterpoints': 1,
        'legend.labelspacing': 0.25,
        'legend.markerscale': 1,
        'legend.handletextpad': 0.5,  # pad between handle and text
        'legend.borderaxespad': 0.5,  # pad between legend and axes
        'legend.borderpad': 0.5,  # pad between legend and legend content
        'legend.columnspacing': 0.75,  # pad between each legend column
        # 'text.fontsize' : 8,

        'xtick.labelsize': 8,
        'ytick.labelsize': 8,

        'xtick.direction': 'in',
        'xtick.major.size': 2.5,
        'xtick.major.width': 0.5,
        'xtick.minor.size': 1.5,
        'xtick.minor.width': 0.5,
        'xtick.minor.visible': True,
        'xtick.minor.bottom': True,

        'xtick.top': True,

        'ytick.direction': 'in',
        'ytick.major.size': 2.5,
        'ytick.major.width': 0.5,
        'ytick.minor.size': 1.5,
        'ytick.minor.width': 0.5,
        'ytick.minor.visible': True,
        'ytick.right': True,

        'lines.linewidth': 0.7,
        'lines.markersize': 3,

        # 'lines.markeredgewidth' : 0,
        # 0 will make line-type markers, such as '+', 'x', invisible
        'axes.autolimit_mode': 'round_numbers',
        'axes.xmargin': 0,
        'axes.ymargin': 0,
        'xtick.direction': 'in',
        'xtick.top': True,
        'ytick.direction' : 'in',
        'ytick.right': True,
        }

for _param in _params:
    plt.rcParams[_param] = _params[_param]