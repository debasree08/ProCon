"""
loader.py
---------------------------------------
Dataset loading utilities for ProCon-m.

Author: Debasree Das
"""

from pathlib import Path
import pandas as pd


class DatasetLoader:
    """
    Loads a single recording from the inD/exiD dataset.

    Parameters
    ----------
    dataset_path : str or Path
        Path containing the recording files.
    """

    def __init__(self, dataset_path):

        self.dataset_path = Path(dataset_path)

    def load_recording_meta(self, recording_id):

        filename = self.dataset_path / f"{recording_id:02d}_recordingMeta.csv"

        return pd.read_csv(filename)

    def load_tracks(self, recording_id):

        filename = self.dataset_path / f"{recording_id:02d}_tracks.csv"

        return pd.read_csv(filename)

    def load_tracks_meta(self, recording_id):

        filename = self.dataset_path / f"{recording_id:02d}_tracksMeta.csv"

        return pd.read_csv(filename)

    def load_recording(self, recording_id):
        """
        Loads and merges all files belonging to one recording.
        """

        tracks = self.load_tracks(recording_id)

        tracks_meta = self.load_tracks_meta(recording_id)

        recording_meta = self.load_recording_meta(recording_id)

        tracks = tracks.merge(
            tracks_meta,
            on=["recordingId", "trackId"],
            how="left"
        )

        return tracks, recording_meta