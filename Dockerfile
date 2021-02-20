FROM python:3.8.7

COPY ./src /src
RUN pip install /src && rm -fr /src
CMD /bin/bash