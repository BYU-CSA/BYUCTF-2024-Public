# Gaming
Description:
```markdown
`gaming.chal.cyberjousting.com:1361`
```

## Writeup
This challenge runs on a Velocity Minecraft proxy, which is basically acts like a regular Minecraft server except we didn't configure it so that you can play on it.

When you see a Minecraft server on the multiplayer screen, it requests the status of the Minecraft server to get the supported versions, MOTD (Message of the Day), and server icon for each server in your list. 
 
However, there is another kind of request you can make to a Minecraft server: [a query](https://wiki.vg/Query#Example_implementations). Minecraft clients don't perform this natively, but there are other programs that make these requests. (Modded clients may also use this kind of request, but I'm not sure.) For instance, [MCStatus](https://github.com/py-mine/mcstatus) is a Python module that can both check the status of and make queries to Minecraft servers. 

However, this program only allows you to perform a 'full stat' query. This usually has everything a 'basic stat' query does and more, but this CTF is configured to only send back the flag if the user makes a 'basic stat' query. 

You can make a 'basic stat' query with programs like [MineQuery](https://github.com/dreamscached/minequery) or [MCQuery](https://github.com/barneygale/MCQuery) (which was made for an older version of Python but can be fixed by adding 'b' in front of every string containing binary data) or by reverse engineering the protocol yourself. Here's an example of solving the challenge with MCQuery:

```python
server = MCQuery("gaming.chal.cyberjousting.com",1361)
query = server.basic_stat()
print(query)
```

You can also solve using `solve.py`.

**Flag** - `byuctf{th1s!s@Gr8tgam3}`

## Hosting
This challenge should be a Docker container that runs SSH on port 22. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```