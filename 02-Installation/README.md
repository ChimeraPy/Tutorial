# Installation
Activate the virtual environment you created in the previous step:

```bash
$ conda activate chimerapy-tutorial
```

## System Dependencies
Install the system level dependencies for ChimeraPy:

### Linux/ Ubuntu
```bash
$ sudo apt-get install ffmpeg libsm6 libxext6 -y
$ sudo apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev portaudio19-dev python3-pyaudio -y
```

### Windows
Install the C++ build tools for Visual Studio 2019 from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

### Mac (M1 or M2 chips are not supported yet)
1. portaudio: https://formulae.brew.sh/formula/portaudio
2. libjpeg-turbo: https://formulae.brew.sh/formula/jpeg-turbo


The `main` branch has the latest updates and features we want to use for the tutorial. Evenetually, we will publish both packages listed below to `pypi` and `conda`. For installation, run the following commands (in your virtual environment):

```bash
$ conda activate chimerapy-tutorial
$ git clone https://github.com/oele-isis-vanderbilt/ChimeraPy.git
$ cd ChimeraPy
$ pip install -e ".[test]"
$ cd ..
$ git clone https://github.com/oele-isis-vanderbilt/ChimeraPyOrchestrator.git
$ cd ChimeraPyOrchestrator
$ pip install -e ".[test]"
```


### ChimeraPy CLI introduction
Installation provides  `cp-orchestrator` command:

```shell
$ cp-orchestrator --help
usage: The CP orchestrator [-h] {orchestrate,orchestrate-worker,list-remote-workers,server} ...

options:
  -h, --help            show this help message and exit

subcommands:
  valid subcommands

  {orchestrate,orchestrate-worker,list-remote-workers,server}
    orchestrate         Orchestrate the pipeline
    orchestrate-worker  Orchestrate a worker
    list-remote-workers
                        List the remote workers
    server              Start the server
```