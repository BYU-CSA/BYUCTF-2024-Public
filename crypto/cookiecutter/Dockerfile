FROM python:3.12-slim

# dependencies
RUN apt-get update -y
RUN apt-get upgrade -y 
RUN apt-get install dnsutils -y
RUN rm -rf /var/lib/apt/lists/*
RUN pip3 install flask pycryptodome

# setup unpriv user
RUN mkdir /ctf
RUN useradd -M -d /ctf ctf

# copy files
COPY . .

# file perms
RUN chown -R root:ctf /ctf 
RUN chmod -R 750 /ctf

# run
USER ctf
CMD ["python3", "server.py"]
EXPOSE 1337