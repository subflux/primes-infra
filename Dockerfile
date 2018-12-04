FROM centos:7
MAINTAINER subflux@gmail.com

USER root
COPY primes.py /usr/local/bin/
RUN ln -s /usr/local/bin/primes.py /
ENTRYPOINT ["primes.py"]
CMD ["5"]
