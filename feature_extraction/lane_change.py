"""
lane_change.py
---------------------------------------
Lane change detection.
"""

import numpy as np
import pandas as pd

from .base import FeatureExtractor


class LaneChangeDetector(FeatureExtractor):

    def __init__(self,
                 heading_threshold=8):
        """
        Parameters
        ----------
        heading_threshold : float
            Heading variation threshold (degrees).
        """
        self.heading_threshold = heading_threshold

    def compute(self,
                trajectory: pd.DataFrame):

        heading = trajectory["heading"]

        delta_heading = heading.diff().fillna(0)

        lateral_velocity = trajectory["yVelocity"]

        labels = (
            (np.abs(delta_heading) > self.heading_threshold)
            &
            (np.abs(lateral_velocity) > 0.5)
        ).astype(int)

        return pd.Series(
            labels,
            index=trajectory.index,
            name="lane_change"
        )