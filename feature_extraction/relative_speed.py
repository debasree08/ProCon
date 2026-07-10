"""
relative_speed.py
---------------------------------------
Relative speed estimation.
"""

import numpy as np
import pandas as pd

from .base import FeatureExtractor


class RelativeSpeedDetector(FeatureExtractor):

    def __init__(self,
                 speed_threshold=5):
        """
        Parameters
        ----------
        speed_threshold : float
            Relative speed threshold (m/s).
        """
        self.speed_threshold = speed_threshold

    def compute(self,
                trajectory: pd.DataFrame):

        if "peerSpeed" not in trajectory.columns:
            raise ValueError(
                "peerSpeed column not found."
            )

        ego_speed = np.sqrt(
            trajectory["xVelocity"]**2 +
            trajectory["yVelocity"]**2
        )

        relative_speed = abs(
            ego_speed - trajectory["peerSpeed"]
        )

        labels = (
            relative_speed > self.speed_threshold
        ).astype(int)

        return pd.Series(
            labels,
            index=trajectory.index,
            name="relative_speed"
        )