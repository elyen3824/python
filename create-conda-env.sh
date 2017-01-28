#!/bin/bash
/root/miniconda/bin/conda create -q -n py3 python=3 ipython
cd /root/miniconda/bin/
source activate py3
cd /workspace/
pip install pandas
pip install matplotlib