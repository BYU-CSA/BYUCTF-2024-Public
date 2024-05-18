FROM python:3.9

COPY images /srv/images

ENV RANDOM_DIR LF3ngxCuqzELscNPjGHGQiYRQyciU6cD
WORKDIR /usr/src/app/$RANDOM_DIR
COPY src .

RUN pip install --no-cache-dir disnake
ENV TOKEN='MTIyMzgzMjAzNjgwOTI0ODc4OQ.Gn6C89.muic5Sd00l2xdMc8kqz1PTuKKXp76__hsamNVc'

RUN useradd ctf
RUN chown -R ctf:ctf /usr/src/app/$RANDOM_DIR
RUN chmod -R 500 /usr/src/app/$RANDOM_DIR
RUN chown -R ctf:ctf /srv/images
RUN chmod -R 500 /srv/images
USER ctf
CMD [ "python", "main.py" ]