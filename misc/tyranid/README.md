# Tyranid
Description:
```markdown
...

`nc tyranid.chal.cyberjousting.com 1360`

[tyranid.zip]
```

## Writeup


**Flag** - `byuctf{pr4153_7h3_3mp3r0r}`

## Hosting
This challenge should be a Docker container that runs the script `script.py` on port 1360 each time a user connects. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```