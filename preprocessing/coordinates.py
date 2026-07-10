"""
timestamps.py
---------------------------------------
Timestamp utilities.
"""

import pandas as pd


class TimestampBuilder:

    def __init__(self, frame_rate):

        self.frame_rate = frame_rate

    def add_timestamp(self, df):

        df = df.copy()

        df["timestamp"] = df["frame"] / self.frame_rate

        return df

    def add_track_times(self, df):

        df = df.copy()

        df["startTime"] = df["initialFrame"] / self.frame_rate

        df["endTime"] = df["finalFrame"] / self.frame_rate

        return df