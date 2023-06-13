# Implementing Custom Nodes (Recording Modalities)
Now that we have the packaging taken care of and understand the basics of implmenting custom nodes, lets create few nodes: (a.) record data from a computer's camera or a predefined video source  (b.) Displays the data on the screen.

The source code is available in the following (a.) [`video_node.py`](./chimerapy-tutorial/chimerapy_tutorial/video_node.py) (b.) [`show_node.py`](./chimerapy-tutorial/chimerapy_tutorial/show_node.py)

After implementation, we will look at registering the nodes with the ChimeraPy framework via entrypoints and executing the pipeline with JSON configuration.
