# Records
Description:
```markdown
Deep within the labyrinthine corridors of the DNS records for `cyberjousting.com` lies a trove of clandestine data, shrouded in mystery and guarded by digital sentinels. Concealed within the intricate web of cyberspace, this critical information holds the key to unlocking secrets of paramount importance.
```

## Writeup
Use `dig` to look at common subdomains. Under the `www` subdomain there is a flag in one of the TXT records as a base64 encoded string. 

**Flag** - `byuctf{DN5_R3con_M45t3r}`