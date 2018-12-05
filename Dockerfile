FROM centos:7
MAINTAINER subflux@gmail.com

USER root
RUN pwd
RUN ls
RUN mkdir /opt/primes/
COPY primes.py /opt/primes/
COPY requirements.txt /opt/primes/
RUN adduser primes \
 && chown primes:primes /opt/primes/primes.py
# Would normally install virtualenv, but Docker provides that isolation
RUN yum -y install epel-release  \
 && yum -y install python-pip \
 && pip install -r /opt/primes/requirements.txt
RUN echo "#!/bin/bash" > /entrypoint.sh \
 && echo '/opt/primes/venv/bin/python /opt/primes/primes.py $@' >> /entrypoint.sh
RUN chmod 755 /entrypoint.sh
USER primes
ENTRYPOINT ["/entrypoint.sh"]
CMD [""]
