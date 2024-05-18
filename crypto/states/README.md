# States
Description:
```markdown
I have a favorite state (2-letter abbreviation for a US state) but it's a secret. If you can figure it out from this, I guessss you can know, too

state == 15 mod 31
state == 19 mod 23
state == 11 mod 47

Flag format - `byuctf{fullstatename}` (case insensitive)
```

## Writeup
This challenge is based on the Chinese Remainder Theorem, which says that if you know a couple different remainders of Euclidian divisions (divisions with a remainder), and all of those integers are pairwise coprime (`gcd(x, y) == 1`), you can deduce mathematically the initial number.

In this example, we have enough information to deduce the final number, we just need to have a script for it
Here is one implementation:

```python
def chinese_remainder(b, n): 
    bi = b

    N = 1
    for num in n:
        N *= num

    Ni = []
    i = 0
    while i < len(n):
        Ni.append(N // n[i])
        i += 1

    xi = []
    i = 0
    while i < len(n):
        mod = n[i]
        pre = Ni[i] % mod
        incr = 1
        while True:
            if (pre * incr) % mod == 1:
                break
            incr += 1
        xi.append(incr)
        i += 1
    
    x = 0
    i = 0
    while i < len(n):
        x += bi[i] * Ni[i] * xi[i]
        i += 1
    return x % N
```

I won't explain any of the math, but you can find similar scripts to solve the Chinese Remainder Theorem on sites like [W3Schools](https://www.geeksforgeeks.org/implementation-of-chinese-remainder-theorem-inverse-modulo-based-implementation/). After running this script on our numbers with `chinese_remainder([15, 19, 11], [31, 23, 47])`, formatted with the remainders, then moduli in order, we get our result: 387. We know that this needs to be in the format of a state, however, and since the states have every letter from A to Z, we can take this number and determine its value in base 36 (to incorporate the entire alphabet in the possible digits). I wrote a script to solve this:

```python
def tob36(decimal_num):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final = ""

    while decimal_num:
        decimal_num, remainder = divmod(decimal_num, 36)
        final = digits[remainder] + final
    
    return final
```

When we run `387` through this function with `tob36(387)`, we get our answer! `AR`

**Flag** - `byuctf{arkansas}`