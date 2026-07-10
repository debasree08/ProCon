from dataclasses import dataclass


@dataclass
class FeatureVector:

    turn: list

    stop: list

    lane_change: list

    jerkiness: list

    relative_speed: list

    relative_distance: list