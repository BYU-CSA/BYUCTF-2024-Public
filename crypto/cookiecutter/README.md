# Cookie Cutter
Description:
```markdown
I know there are a bunch of vulnerabilities with JWT, so I wanted to use a different implementation to not leave my site vulnerable. This is my best shot.

https://cookiecutter.chal.cyberjousting.com

[server.py]
```

## Writeup

```python
import requests
from base64 import b64decode, b64encode

url = "https://cookiecutter.chal.cyberjousting.com/"
login = "login"
auth = "authenticate"

emaillen = 16 - len("email=")
padlen = 16 - len("admin")
payload = "x" * emaillen + "admin" + chr(padlen) * padlen
encryptedadmin = b64decode(requests.post(url + login, data={'email' : payload }).cookies['cookie'].encode())
# may need to increase the size of the uid field to accomodate more users solving the challenge
padlen = 16 - len("email=&uid=00000&role=") % 16
enc = b64decode(requests.post(url + login, data={'email' : "x" * padlen }).cookies['cookie'].encode())

adminuser = b64encode(enc[:32] + encryptedadmin[16:32]).decode()
flag = requests.get(url + auth, cookies={'cookie' : adminuser}).text
print(flag)
```


**Flag** - `byuctf{d0nt_cut_1t_l1k3_th4t!!}`
