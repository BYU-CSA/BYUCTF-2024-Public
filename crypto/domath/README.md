# Do Math!
Description:
```markdown
We need to... do math... as cybersecurity people?

[domath.py] [hints.txt]
```

## Writeup
Since we are given all of the pieces of RSA in various bits, it's possible to get `p` and `q` by taking the gcd of their respective hints with `n`. Then you can find `n` and `d` from those. Since you already know `e` from the script, you can just quickly reverse it and get the flag! See `solve.py`.

**Flag** - `byuctf{th3_g00d_m4th_1snt_th4t_h4rd}`