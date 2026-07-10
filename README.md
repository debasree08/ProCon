# ProCon-m: When Drivers Cause Ripples: Early Maneuver Detection for Traffic Flow Stability

Urban traffic congestion is not merely a result of high vehicle density but often arises from the cascading ripple effects of localized driving maneuvers that propagate through dense traffic streams. Existing navigation and traffic management systems predominantly rely on reactive strategies that detect congestion post-occurrence and reroute vehicles, often exacerbating congestion propagation rather than preventing it. In this paper, we address the challenge of proactively predicting and mitigating congestion formation by modeling the causal interdependencies among driving maneuvers, traffic flow dynamics, and road context. We present ProCon-m, a multimodal, domain-adaptive, and self-explainable framework that learns how specific maneuvers, such as abrupt stops, lane changes, and turns, interact with traffic density, speed, and road properties to influence congestion emergence. By dynamically pruning maneuver dependencies using information gain and integrating contextual features to estimate ripple potential, ProCon-m recommends congestion-averse driving actions in real time. Extensive evaluations on naturalistic driving datasets from city streets and highways, along with large-scale simulations, demonstrate that ProCon-m can predict congestion up to 30 minutes in advance, mitigate 60–80% of cascading congestion scenarios, and reduce average travel time by 25–44% with minimal route overhead, establishing it as a proactive, behavior-aware framework for anticipatory traffic congestion management.

# Modalities

We utilize two public dataset [1],[2] captured using drone containing information from every vehicle such as the velocity, acceleration, UTM data. A sample dataset is provided with the following modalities inD [1] public dataset. 

More details about the public dataset can be found in the paper [1].

# Dataset Structure

Each recording consists of four CSV files that together describe the road environment, participating vehicles, and their trajectories.

## 1. recordingMeta.csv

This file contains metadata associated with each recording, including the recording location, frame rate, recording duration, speed limit, and map information.

| Field                        | Description                        |
| ---------------------------- | ---------------------------------- |
| `recordingId`                | Unique identifier of the recording |
| `locationId`                 | Intersection/location identifier   |
| `frameRate`                  | Recording frame rate (fps)         |
| `speedLimit`                 | Road speed limit (m/s)             |
| `weekday`                    | Day of recording                   |
| `startTime`                  | Recording start time               |
| `duration`                   | Recording duration (seconds)       |
| `numTracks`                  | Total number of tracked objects    |
| `numVehicles`                | Number of vehicles                 |
| `numVRUs`                    | Number of vulnerable road users    |
| `latLocation`, `lonLocation` | Approximate geographic location    |
| `xUtmOrigin`, `yUtmOrigin`   | UTM origin of the recording        |
| `orthoPxToMeter`             | Pixel-to-meter conversion factor   |

## 2. tracks.csv

This file contains frame-wise trajectory information for every tracked vehicle.

Each row corresponds to one frame of one vehicle.

| Field                                | Description                                         |
| ------------------------------------ | --------------------------------------------------- |
| `recordingId`                        | Recording identifier                                |
| `trackId`                            | Unique vehicle identifier                           |
| `frame`                              | Frame number relative to the start of the recording |
| `trackLifetime`                      | Elapsed lifetime (frames) of the tracked object     |
| `xCenter`, `yCenter`                 | Vehicle center position (UTM coordinates)           |
| `heading`                            | Vehicle heading (degrees)                           |
| `width`, `length`                    | Vehicle dimensions (meters)                         |
| `xVelocity`, `yVelocity`             | Velocity components                                 |
| `xAcceleration`, `yAcceleration`     | Acceleration components                             |
| `lonVelocity`, `latVelocity`         | Longitudinal and lateral velocities                 |
| `lonAcceleration`, `latAcceleration` | Longitudinal and lateral accelerations              |


## 3. tracksMeta.csv

This file stores metadata corresponding to every tracked object.

| Field             | Description                                             |
| ----------------- | ------------------------------------------------------- |
| `recordingId`     | Recording identifier                                    |
| `trackId`         | Vehicle identifier                                      |
| `initialFrame`    | First observed frame                                    |
| `finalFrame`      | Last observed frame                                     |
| `numFrames`       | Total tracked frames                                    |
| `width`, `length` | Vehicle dimensions                                      |
| `class`           | Object category (e.g., car, truck, pedestrian, bicycle) |


Commands to run the model

    python main.py

# References

[1] Julian Bock, Robert Krajewski, Tobias Moers, Steffen Runde, Lennart Vater, and Lutz Eckstein. 2019. The inD Dataset: A Drone Dataset of Naturalistic Road User Trajectories at German Intersections. In IEEE IV. 1929–1934.

[2] Tobias Moers, Lennart Vater, Robert Krajewski, Julian Bock, Adrian Zlocki, and Lutz Eckstein. 2022. The exiD Dataset: A Real-World Trajectory Dataset of Highly Interactive Highway Scenarios in Germany. In IEEE IV. 958–964.
