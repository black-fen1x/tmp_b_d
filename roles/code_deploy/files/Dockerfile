FROM python:3.10
WORKDIR /core
COPY ./core .
COPY ./core/requirements.txt requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
#RUN chmod 755
