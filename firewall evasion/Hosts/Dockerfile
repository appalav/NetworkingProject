FROM handsonsecurity/seed-ubuntu:large
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get -y install openssh-server \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install PySocks
COPY sshd_config /etc/ssh/sshd_config
