# The Worst Challenge Ever
Description:
```markdown
Hello, there

[justterrible.txt]
```

## Writeup
If you look at the bytes of the file, you'll see a lot of null bytes in the middle of the file, and some 1 bytes. With some more experimentation you'll run into the fact that the number of null bytes is directly correlated with some value of letters. If you run a Python script like the one below, you can get the flag. See `solve.py`.

**Flag** - `byuCTF{wh4ts_4_nu11_byt3_4nyw4ys}`