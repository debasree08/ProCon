import numpy as np
import pandas as pd

from .base import FeatureExtractor


class TurnDetector(FeatureExtractor):

    def __init__(self,
                 threshold=35):

        self.threshold = threshold

    def compute(self,
                trajectory: pd.DataFrame):

        heading = trajectory["heading"].values

        turns = np.zeros(len(heading))

        delta = np.diff(heading)

        delta = np.insert(delta,0,0)

        turns[np.abs(delta)>self.threshold]=1

        return pd.Series(turns,
                         index=trajectory.index)