FROM centos:7
MAINTAINER subflux@gmail.com

USER root
RUN cat /etc/redhat-release
ENTRYPOINT ["/bin/echo"]
CMD ["If you add an argument to docker run, I'll print that instead."]
