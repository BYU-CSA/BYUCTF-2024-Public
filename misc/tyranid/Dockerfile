FROM python:3.10-slim

# install dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y xinetd
RUN rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache-dir torch pillow numpy

# setup unpriv user
RUN mkdir /ctf
RUN useradd -M -d /ctf ctf

# copy files
RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY tyranid-detector.py /ctf
COPY flag.txt /ctf
COPY xinetd.sh /ctf/xinetd.sh
COPY sensor-model.pt /ctf/sensor-model.pt
COPY potential-tyranid.png /ctf/potential-tyranid.png

# file perms
RUN chmod -R 750 /ctf
RUN chown -R root:ctf /ctf

# run
CMD ["/usr/sbin/xinetd", "-dontfork"]
EXPOSE 40000