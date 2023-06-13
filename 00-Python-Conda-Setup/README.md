# Python, Conda and Dependencies (A short/brief walkthrough)

Python is an interpreted language widely used in scientific/research computing. Dynamic typing, ease of use and a plethora of ecosystem packages ranging from numbers' manipulation to machine learning make it a popular choice for data scientists and researchers alike. There a ton of great resources on learning Python online. The official [documentation](https://docs.python.org/3/tutorial/index.html) is a great place to start.  

The standard library of Python is quite extensive and powerful, but what makes Python such a great langauge is its ecosystem of third-party libraries - majority of the most popular ones being open source - that make it a viable workhorse for most research projects. However, because of the interpreted nature of the language, using third party libraries, requires a dependency management system. Added on that, over the years, a convention has been established to use virtual environments that isolate project level dependencies, making it easier and more reproducible to run/develop projects. This is where [`conda`](https://github.com/conda/conda): A system-level, binary package and environment manager running on all major operating systems and platforms, comes in. With `conda` users can create, export, list, remove and update environments that have different versions of Python and/or packages installed in them. Switching or moving between environments is called activating the environment. You can also share an environment file. 

## Installing `conda`
To install `conda`, follow the instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), based on the operating system you are using. Additionally, because of the popularity as well as some inefficeincies of `conda`, there are other alternatives such as [micromamba/mamba](https://mamba.readthedocs.io/en/latest/index.html), both of which are drop-in replacements for `conda`, but are in early phases of their evolution. 

## Create a new environment
After installing `conda`, we will create a new environment for the tutorial. To do so, run the following command:

```bash
$ conda create -n chimerapy-tutorial python=3.10 -c conda-forge -c defaults
```

The above command will create a new Python environment named `chimerapy-tutorial`, with Python version 3.10. The `-c` flag is used to specify the channel from which to install the package. The `conda-forge` channel is a community-led collection of recipes, build infrastructure and distributions for the `conda` package manager. The `defaults` channel is the primary channel for `conda` packages. You can activate the environment by running:

```bash
$ conda activate chimerapy-tutorial
```