# CLI and Pipeline Execution Configuration

## Registering Nodes
The nodes can be registered with the ChimeraPy framework via entrypoints. The entrypoint group is `chimerapy_orchestrator.nodes_registry` and the entrypoint name is the name of the node. The entrypoint should return a callable that returns a dictionary of metadata and module info about the exported nodes. For the tutorial package, see [`__init__.py`](./chimerapy-tutorial/chimerapy_tutorial/__init__.py) and [`pyproject.toml`](./chimerapy-tutorial/pyproject.toml) for the node registry.


## Pipeline Configuration
The pipeline execution configuration is tabulated below and can be used to create a JSON configuration for the pipeline.

### Pipeline Config
| name | default | description                                                                   |
|-----|-----|-------------------------------------------------------------------------------|
| mode | record | The mode of the pipeline_service.                                             |
| name | Pipeline | The name of the pipeline                                                      |
| description |  | The description of the pipeline.                                              |
| workers | None | The workers to be added. See WorkerConfig                                     |
| nodes | None | The nodes in the pipeline_service. See NodeConfig                             |
| adj | None | The edge list of the pipeline_service graph.                                  |
| manager_config | None | The manager configs.                                                          |
| mappings | None | The delegation mapping of workers to nodes.                                   |
| discover_nodes_from | [] | The list of modules to discover nodes from. Deprecated. see NodeConfig.package. |
| timeouts | commit_timeout=60 preview_timeout=20 record_timeout=20 collect_timeout=20 stop_timeout=20 shutdown_timeout=20 | The timeouts for the pipeline operation.                                      |

### WorkerConfig

| name | default | description |
|-----|-----|-----|
| name | None | The name of the worker. |
| id | None | The id of the worker. |
| remote | False | Indicating the worker is remote and is connected(no creation needed). |
| description |  | The description of the worker. |

### NodeConfig

| name | default | description |
|-----|-----|-----|
| registry_name | None | The name of the node to search in the registry. |
| name | None | The name of the node. |
| kwargs | {} | The kwargs for the node. |
| package | None | The package that registered this node. |

## Example Configuration File
An example configuration file can be found [here](./chimerapy-tutorial/orchestration-configs/video-show.json)

## Executing the Pipeline from CLI

```shell
$ cp-orchestrator orchestrate --config chimerapy-tutorial/orchestration-configs/video-show.json  
```

