__version__ = "0.0.1"


def register_nodes_metadata():
    return {
        "description": "A repository of sharable chimerapy nodes with different functionalities.",
        "nodes": [
            "chimerapy_tutorial.video_node:Video",
            "chimerapy_tutorial.show_node:ShowWindows",
            "chimerapy_tutorial.yolo:YOLONode",
        ],
    }
