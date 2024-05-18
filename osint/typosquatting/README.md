# TypoSquatting
Description:
```markdown
Uh oh! A popular social media site may be the victim of typosquatting. The social media owners might want to fix that so their users don't accidentally go to the wrong site. When does the registration for the `facebooks.com` domain expire? Maybe after it expires, the real company could take control...

Flag format - `byuctf{YYYY-MM-DD}` (ie, `byuctf{1994-12-30}`)
```

## Writeup
Perform a whois lookup on the domain `facebooks.com`. I used the whois.com website. Check for the field that says "Expires On", and the date is already listed in the `YYYY-MM-DD` format, so the date just needs to be wrapped in the flag.

**Flag** - `byuctf{2025-04-10}`