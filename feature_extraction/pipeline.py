from .turn import TurnDetector
from .stop import StopDetector
from .lane_change import LaneChangeDetector
from .jerkiness import JerkinessDetector
from .relative_speed import RelativeSpeedDetector
from .relative_distance import RelativeDistanceDetector

from .feature_vector import FeatureVector


class FeaturePipeline:

    def __init__(self):

        self.turn = TurnDetector()

        self.stop = StopDetector()

        self.lane = LaneChangeDetector()

        self.jerk = JerkinessDetector()

        self.speed = RelativeSpeedDetector()

        self.distance = RelativeDistanceDetector()

    def run(self,
            trajectory):

        return FeatureVector(

            turn=self.turn.compute(trajectory),

            stop=self.stop.compute(trajectory),

            lane_change=self.lane.compute(trajectory),

            jerkiness=self.jerk.compute(trajectory),

            relative_speed=self.speed.compute(trajectory),

            relative_distance=self.distance.compute(trajectory)

        )