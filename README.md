# ChimeraPy Tutorial
In this tutorial, we will look at how to use the ChimeraPy to create multimodal data collection pipelines.

## Installation
To install ChimeraPy, you can use `pip` and `conda`:
```bash
$ git clone git@github.com:oele-isis-vanderbilt/ChimeraPyTutorial.git
$ cd chimerapy-tutorial
$ conda create -n chimerapy-tutorial python=3.9
$ conda activate chimerapy-tutorial
$ pip install -e .
```

Download the test data from [here](https://vanderbilt.box.com/s/2xpp0e2uy3mhr1iuipnpbgumf80yqyuu)

## Run using script
```shell
$ python run.py --help
usage: ChimerapyTutorial [-h] [--manager-port MANAGER_PORT] [--manager-logdir MANAGER_LOGDIR] {web_and_screen}

positional arguments:
  {web_and_screen}

optional arguments:
  -h, --help            show this help message and exit
  --manager-port MANAGER_PORT
                        The manager port (default: 9001)
  --manager-logdir MANAGER_LOGDIR
                        The manager logdir (default: runs)
```

## Run with ChimeraPyOrchestrator
```shell
$ cp-orchestrator orchestrate --config orchestration-configs/video-show.json
```