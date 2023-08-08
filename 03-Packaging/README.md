# Packaging and Plugin Architecture

## Creating Package
Now that we have installed the pre-requisites and the necessary dependencies, we can go ahead and start building custom pipelines leveraging the ChimeraPy framework. To be methodical, we will start by creating a python package named `chimerapy-tutorial`. With the following directory structure. 

```bash
chimerapy-tutorial
├── chimerapy_tutorial
│   └── __init__.py
├── LICENSE
├── pyproject.toml
└── setup.py
```
Copy the contents of this [`directory`](./chimerapy-tutorial) into the directory created and install the package.

## Install

```bash
$ cd chimerapy-tutorial
$ pip install -e .
```

## Verify Installation
```shell
>>> import chimerapy_tutorial
>>> chimerapy_tutorial.__version__
'0.0.1'
```

## ChimeraPy Nodes and Plugin Decorators

_copied as is from https://chimerapy.readthedocs.io/en/latest/usage/basics.html#creating-a-custom-node_

For the basics, we start with the smallest component of the system, the Node. The Node provides the container for logic in how to collect, process, and return data within the ChimeraPy framework. Then, we will discuss how to incorporate a Node into the directed acyclic graph (DAG) pipeline through the Graph. We will finish the setup with configuring our local or distributed cluster with Manager and Worker. Once all setup is complete, we can execute the system and control the cluster.

## Creating a Custom Node

To create a custom Node, we overwrite the `setup`, `step`, and `teardown` methods. Below is an example of a Node that generates a sequence of random numbers:

```python
import time
import chimerapy.engine as cpe
import numpy as np

class RandomNode(cpe.Node):

    def setup(self):
        # Create the generator to be used later
        self.rng = np.random.default_rng(0)

    def step(self):
        # Set the execution to 1 every second
        time.sleep(1)
        return self.rng.random()

    def teardown(self):
        # Not necessary here, but can be used to close
        # files or disconnect from devices.
        del self.rng
```

It is important to remember that there is three possible node types: source, step, and sink. This is the taxonomy:

* Source: no inputs, yes outputs

* Step: yes inputs, yes outputs

* Sink: yes inputs, no outputs

For this example, the RandomNode is a source node. Step and sink have a step(self, data: Dict[str, DataChunk]) method to retrieve input datas. Since source Node do not have inputs, it has a simplified step(self) method instead.

## The DataChunk Container
A main attribute of ChimeraPy is that it does not assume what type of data is being transmitted between Nodes. Therefore, when developing your custom node implementations, the step function can return anything that is serializable. There are moments when this isn’t beneficial. For example, to make video streaming work in real time, it is required to compress video frames with an algorithm optimized for images. This implies that ChimeraPy must then know what is being transmitted. This is achieved through the use of the DataChunk container. This is an example for a video streaming Node:

```python
class ScreenCapture(cpe.Node):

    def step(self) -> cpe.DataChunk:

        time.sleep(1 / 10)
        frame = cv2.cvtColor(
            np.array(ImageGrab.grab(), dtype=np.uint8), cv2.COLOR_RGB2BGR
        )

        # Create container and send it
        data_chunk = cpe.DataChunk()
        data_chunk.add("frame", frame, "image")
        return data_chunk
```

As of now, the only special compression algorithms incorporated into ChimeraPy are for images. When transmitting images, use the DataChunk with the image content-type option. Otherwise, ChimeraPy will mark the Node’s output as other and will apply a generic serialization and compression method.

## The Plugin Decorators
To make the Node available to the ChimeraPy framework, we must register it with the plugin decorators. The decorators are used to register the Node with the ChimeraPy framework. The decorators are `@source_node`, `@sink_node` and `@step_node`, which are used to register source, sink and step nodes respectively. The decorators take the following arguments:

```python
1. name: name of the nodes in the registry 
2. add_to_registry: whether to add the node to the registry (default = False)
```

For the node implementation above, we would register it as follows:

```python
from chimerapy_orchestrator.registry.utils import source_node

@source_node(name="ChimeraPyTutorial_RandomNode", add_to_registry=False)
class RandomNode(cpe.Node):
    ...
```

## Discovery Mechanism via EntryPoints
For the subsequent step, we will look at entrypoints to register custom nodes and execute pipelines from the ChimeraPy CLI. 