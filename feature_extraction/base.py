from abc import ABC, abstractmethod
import pandas as pd


class FeatureExtractor(ABC):
    """
    Base class for all feature extractors.
    """

    @abstractmethod
    def compute(self,
                trajectory: pd.DataFrame):
        """
        Computes feature for a single trajectory.

        Parameters
        ----------
        trajectory : pandas.DataFrame

        Returns
        -------
        pandas.Series
        """
        pass