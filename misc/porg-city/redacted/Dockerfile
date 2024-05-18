FROM python:3.9

COPY images /srv/images

ENV RANDOM_DIR this_is_randomized_in_production
WORKDIR /usr/src/app/$RANDOM_DIR
COPY src .

RUN pip install --no-cache-dir disnake
ENV TOKEN='REDACTED'

RUN useradd ctf
RUN chown -R ctf:ctf /usr/src/app/$RANDOM_DIR
RUN chmod -R 500 /usr/src/app/$RANDOM_DIR
RUN chown -R ctf:ctf /srv/images
RUN chmod -R 500 /srv/images
USER ctf
CMD [ "python", "main.py" ]