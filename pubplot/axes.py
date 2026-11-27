# -*- coding: utf-8 -*-
"""
axes.py
=======

Helpers to apply to an Axes after plotting.

The APS parameters use zero margins and round-number limits, so data points that
sit exactly on an axis limit are cut in half by the frame. ``unclip`` draws them in
full and keeps the limits; ``pad`` moves the limits outward instead.

"""

import numpy as np
from matplotlib.collections import Collection
from matplotlib.lines import Line2D

__all__ = ['unclip', 'pad']


def _data_points(artist, ax):
    """Return the (N, 2) data-space points of ``artist``, or None if it is not
    drawn in data coordinates."""
    if isinstance(artist, Line2D):
        if artist.get_transform() is not ax.transData:
            return None  # e.g. axhline / axvline, partly in axes coordinates
        return artist.get_xydata()
    if isinstance(artist, Collection):
        offsets = np.asarray(artist.get_offsets())
        if len(offsets) and artist.get_offset_transform() is ax.transData:
            return offsets  # scatter: markers placed at offsets
        if artist.get_transform() is ax.transData:
            paths = artist.get_paths()
            if paths:
                return np.concatenate([p.vertices for p in paths])
    return None


def _within(values, lim):
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    if values.size == 0:
        return False
    lo, hi = min(lim), max(lim)
    tol = 1e-9 * (hi - lo)
    return bool(np.all((values >= lo - tol) & (values <= hi + tol)))


def unclip(ax):
    """
    Draw markers that sit on the axes frame in full instead of cut in half.

    Turns off clipping for every line and collection on ``ax`` whose data lie
    entirely inside the current axis limits, so nothing is drawn outside the
    frame. Artists that extend past the limits stay clipped. Call it after the
    last ``set_xlim`` / ``set_ylim``.

    Usage::

      ax.plot(x, y, **next(linestyles))
      pubplot.unclip(ax)

    :param ax: the axes to fix
    :type ax: matplotlib.axes.Axes
    :return: the artists whose clipping was turned off
    :rtype: list
    """
    xlim, ylim = ax.get_xlim(), ax.get_ylim()  # also finalises autoscaling
    unclipped = []
    for artist in list(ax.lines) + list(ax.collections):
        points = _data_points(artist, ax)
        if points is None:
            continue
        points = np.asarray(points, dtype=float)
        if len(points) == 0:
            continue
        if _within(points[:, 0], xlim) and _within(points[:, 1], ylim):
            artist.set_clip_on(False)
            unclipped.append(artist)
    return unclipped


def pad(ax, fraction=0.02, axis='both'):
    """
    Move the axis limits outward by ``fraction`` of their span.

    An alternative to ``unclip``: markers on the old limits are no longer cut,
    but the frame no longer sits on round tick values. Log axes are padded in
    log space. Autoscaling is turned off for the padded axes.

    :param ax: the axes to pad
    :type ax: matplotlib.axes.Axes
    :param fraction: padding on each side, as a fraction of the axis span
    :type fraction: float
    :param axis: 'x', 'y' or 'both'
    :type axis: str
    """
    if axis not in ('x', 'y', 'both'):
        raise ValueError("axis must be 'x', 'y' or 'both', not %r" % (axis,))
    names = ('x', 'y') if axis == 'both' else (axis,)
    for name in names:
        scale = getattr(ax, name + 'axis').get_transform()
        lo, hi = scale.transform(np.asarray(getattr(ax, 'get_%slim' % name)()))
        delta = fraction * (hi - lo)
        new = scale.inverted().transform(np.array([lo - delta, hi + delta]))
        getattr(ax, 'set_%slim' % name)(*new)
