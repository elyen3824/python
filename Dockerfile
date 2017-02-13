FROM continuumio/anaconda
MAINTAINER myself

# Add code directory containing application code
ADD . /code

#switch working directory to /code folder
WORKDIR /code

# Creating environment (sandbox instance called py3 [choose the name you want])
RUN conda create -q -n py3 python=3 ipython

# Activating created environment
RUN /bin/bash -c "source activate py3"

# Install package manager pip
RUN conda install -q pip

# which ipython is to be used in the environment? pip freeze shows it
RUN pip freeze

# Installing ipython notebook
RUN conda install -q ipython-notebook

# Installing the packages
RUN pip install -q numpy
RUN pip install -q pandas
RUN pip install -q matplotlib

CMD ["python", "price_plot.py"]
