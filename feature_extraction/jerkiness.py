"""
jerkiness.py
---------------------------------------
Detect abrupt changes in acceleration (jerkiness).
"""

import numpy as np
import pandas as pd

from .base import FeatureExtractor


class JerkinessDetector(FeatureExtractor):
    """
    Detects jerkiness from longitudinal and lateral acceleration.
    """

    def __init__(self,
                 jerk_threshold=2.5):
        """
        Parameters
        ----------
        jerk_threshold : float
            Threshold (m/s^3) above which jerk is considered unsafe.
        """
        self.jerk_threshold = jerk_threshold

    def compute(self,
                trajectory: pd.DataFrame):

        dt = trajectory["timestamp"].diff().fillna(0.04)

        ax = trajectory["xAcceleration"]
        ay = trajectory["yAcceleration"]

        jerk_x = ax.diff() / dt
        jerk_y = ay.diff() / dt

        jerk = np.sqrt(jerk_x**2 + jerk_y**2)
        jerk = jerk.fillna(0)

        labels = (jerk > self.jerk_threshold).astype(int)

        return pd.Series(labels,
                         index=trajectory.index,
                         name="jerkiness")