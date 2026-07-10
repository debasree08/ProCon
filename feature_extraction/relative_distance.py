"""
relative_distance.py
---------------------------------------
Relative distance estimation.
"""

import pandas as pd

from .base import FeatureExtractor


class RelativeDistanceDetector(FeatureExtractor):

    def __init__(self,
                 safe_distance=5):
        """
        Parameters
        ----------
        safe_distance : float
            Minimum safe distance (meters).
        """
        self.safe_distance = safe_distance

    def compute(self,
                trajectory: pd.DataFrame):

        if "peerDistance" not in trajectory.columns:
            raise ValueError(
                "peerDistance column not found."
            )

        labels = (
            trajectory["peerDistance"] < self.safe_distance
        ).astype(int)

        return pd.Series(
            labels,
            index=trajectory.index,
            name="relative_distance"
        )