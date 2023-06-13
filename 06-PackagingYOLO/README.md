# Packaging YOLO

## Pre-requisites
Install [`torch`](https://pytorch.org/get-started/locally/) and run
```shell
$ pip install yolov5
```

## Creating optional dependencies for YOLO
First, we need to create an optional dependency for yolo, see [`pyproject.toml`](./chimerapy-tutorial/pyproject.toml) for details.

## Implementation of Yolo Node
Now we have dependencies handled, we can implement a custom node for YOLO. See [`yolo.py`](./chimerapy-tutorial/chimerapy_tutorial/yolo.py) for implementation. The implementation detects people in a video frame and displays them. Notice to use of custom data types for output inside the datachunk container.

## Example configuration and execution
See [yolo.json](./chimerapy-tutorial/orchestration-configs/yolo.json) for the configuration. To execute the pipeline, run:
```shell
$ cp-orchestrator orchestrate --config chimerapy-tutorial/orchestration-configs/yolo.json
```