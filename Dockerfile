FROM centos:7
MAINTAINER subflux@gmail.com

USER root
RUN pwd
RUN ls
RUN mkdir /opt/primes/
COPY primes.py /opt/primes/
COPY requirements.txt /opt/primes/
RUN ln -s /opt/primes/primes.py /
RUN adduser primes
RUN chown primes:primes /opt/primes/primes.py
# Not necessery on Docker, but possibly less overhead than installing
# the RHEL SCL which contains `pip`.
RUN yum -y install python-virtualenv
RUN virtualenv /opt/primes/venv
RUN /opt/primes/venv/bin/pip install -r /opt/primes/requirements.txt
RUN echo "#!/bin/bash" > /entrypoint.sh
RUN echo /opt/primes/venv/bin/python /opt/primes/primes.py >> /entrypoint.sh
RUN chmod 755 /entrypoint.sh
USER primes
ENTRYPOINT ["/entrypoint.sh"]
CMD ["5"]
