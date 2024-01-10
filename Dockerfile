# pull official base image
FROM --platform=linux/amd64 python:3.12.1-bookworm

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


#INSTALL system dependency and miniconda
RUN apt-get update \
    && apt-get install -y netcat-traditional \
    && apt-get install -y build-essential \
    && apt-get install -y wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH
# install dependencies
RUN conda create --name cashopower pip
RUN pip install imutils

#RUN conda install -c conda-forge opencv
#RUN conda install -c conda-forge dlib
RUN conda install -c conda-forge pandas
RUN conda install -c conda-forge scikit-learn
RUN conda install -c conda-forge Django
RUN conda install -c conda-forge pillow
RUN conda install -c conda-forge psycopg2
RUN conda install -c conda-forge djangorestframework

RUN pip install djangorestframework-simplejwt
RUN pip install django-filter
RUN pip install gunicorn

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]