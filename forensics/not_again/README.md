# Not again! I've been BitLockered out of my own computer!
Description:
```markdown
Install Bitlocker they said... it will protect your data they said... Well, now I don't have access to any of my data because I forgot my password... again! Can you find my FVEK keys? I managed to capture my RAM so they should be in there

Flag format - `byuctf{key1_key2_key3}` (order not significant)

* Mirror 1 - https://byu.box.com/s/paexcd1t1er8bj435gg88i52q9ho8ftf
* Mirror 2 - https://drive.google.com/file/d/1EAYpFu0ULc4fGt2qNoJTaNvG4F9A8Vw7/view?usp=sharing
```

## Writeup
Using Volatility 2, you can find a tool called `bitlocker.py` that will parse out the keys for you. You can also use the Ubuntu SANS SIFT Workstation which has Vol 2 and bitlocker plugin already installed to recover the three keys.

**Flags**:
* `byuctf{968052b6b247b32f6cfecce39749785f_91c75f658705c36090f03779cacb056179e16316ee4af1e90d0f84e090b88d8b_91d4cceb5bf238cb3cb96367314773f5}`
* `byuctf{968052b6b247b32f6cfecce39749785f_91d4cceb5bf238cb3cb96367314773f5_91c75f658705c36090f03779cacb056179e16316ee4af1e90d0f84e090b88d8b}`
* `byuctf{91d4cceb5bf238cb3cb96367314773f5_968052b6b247b32f6cfecce39749785f_91c75f658705c36090f03779cacb056179e16316ee4af1e90d0f84e090b88d8b}`
* `byuctf{91d4cceb5bf238cb3cb96367314773f5_91c75f658705c36090f03779cacb056179e16316ee4af1e90d0f84e090b88d8b_968052b6b247b32f6cfecce39749785f}`
* `byuctf{91c75f658705c36090f03779cacb056179e16316ee4af1e90d0f84e090b88d8b_91d4cceb5bf238cb3cb96367314773f5_968052b6b247b32f6cfecce39749785f}`
* `byuctf{91c75f658705c36090f03779cacb056179e16316ee4af1e90d0f84e090b88d8b_968052b6b247b32f6cfecce39749785f_91d4cceb5bf238cb3cb96367314773f5}`