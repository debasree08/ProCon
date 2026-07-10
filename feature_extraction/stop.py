import numpy as np
import pandas as pd

from .base import FeatureExtractor


class StopDetector(FeatureExtractor):

    def __init__(self,
                 speed_threshold=0.5):

        self.speed_threshold = speed_threshold

    def compute(self,
                trajectory):

        speed = np.sqrt(

            trajectory["xVelocity"]**2 +

            trajectory["yVelocity"]**2

        )

        stop = (speed<self.speed_threshold).astype(int)

        return stop