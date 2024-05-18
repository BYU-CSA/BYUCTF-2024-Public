FROM python:3

# install dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y xinetd
RUN rm -rf /var/lib/apt/lists/*
RUN pip3 install gensim
RUN pip3 install nltk
RUN pip3 install "scipy<1.13"

# setup unpriv user
RUN mkdir /ctf
RUN useradd -M -d /ctf ctf

# copy files
RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY script.py /ctf
COPY flag.txt /ctf
COPY xinetd.sh /ctf/xinetd.sh
COPY liberal_model.d2v /ctf
COPY conservative_model.d2v /ctf
COPY punkt /ctf/nltk_data/tokenizers/punkt

ENV NLTK_DATA=/ctf/nltk_data

# file perms
RUN chmod -R 750 /ctf
RUN chown -R root:ctf /ctf

# run
CMD ["/usr/sbin/xinetd", "-dontfork"]
EXPOSE 40000