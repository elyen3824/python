#! /bin/bash
export PATH=$PATH:/root/anaconda/bin

# Creating environment (sandbox instance called py3 [choose the name you want])
conda create -q -n py3 python=3 ipython

# Activating created environment
source activate py3

# Install package manager pip
conda install -q pip

# The installation installs the packages
#pip install numpy
#pip install pandas
#pip install matplotlib

# which ipython is to be used in the environment? pip freeze shows it
pip freeze

# Installing ipython notebook
conda install -q ipython-notebook

# Installing the packages
pip install -q numpy
pip install -q pandas
pip install -q matplotlib