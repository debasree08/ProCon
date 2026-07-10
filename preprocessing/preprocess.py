from .loader import DatasetLoader
from .timestamps import TimestampBuilder
from .coordinates import CoordinateConverter
from .smoothing import SignalPreprocessor


class TrajectoryPreprocessor:

    def __init__(self, dataset_path):

        self.loader = DatasetLoader(dataset_path)

    def process(self, recording_id):

        tracks, meta = self.loader.load_recording(recording_id)

        fps = meta.loc[0, "frameRate"]

        timestamp = TimestampBuilder(fps)

        tracks = timestamp.add_timestamp(tracks)

        tracks = timestamp.add_track_times(tracks)

        converter = CoordinateConverter()

        tracks = converter.dataframe_to_gps(
            tracks,
            meta.loc[0, "xUtmOrigin"],
            meta.loc[0, "yUtmOrigin"]
        )

        return tracks