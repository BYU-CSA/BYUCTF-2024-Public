# Austen Supremacy
Description:
```markdown
Lydia loves Jane Austen. In fact, her favorite book is Pride and Prejudice. Her and her friends like to talk about the book together, but recently Lydia has started encoding her messages. Unfortunately Lydia's friends don't understand her secret code -- could you help them out and identify the secret message? 

Flag format - `byuctf{secretmessage}`

`1.1.1 8.9.8 10.2.11 4.14.28 61.2.4 47.10.3 23.7.37 41.12.4 17.6.10 1.1.21`
```

## Writeup
This is a standard cipher in which the numbers reference specific letters in a book. The book here is obviously Pride and Prejudice. The book is in the public domain so it can be found online. 

The numbers stand for `CHAPTER.PARAGRAPH.LETTER`. Note that the character references only alphabetic characters, so skip over any punctuation and spaces. Although it is certain that formatting may differ between different editions online, when I searched Google for "pride and prejudice book online", these were the top results and they all have similar formatting. Any of these sites would work for solve the cipher.

* https://www.janeausten.org/pride-and-prejudice/pride-and-prejudice-online.php
* https://www.fulltextarchive.com/book/pride-and-prejudice/
* https://www.gutenberg.org/files/1342/1342-h/1342-h.htm
* https://giove.isti.cnr.it/demo/eread/Libri/joy/Pride.pdf
* https://www.planetebook.com/free-ebooks/pride-and-prejudice.pdf

Below is a direct mapping of each section to the letter represented:

```
1.1.1 (i)
8.9.8 (l)
10.2.11 (o)
4.14.28 (v)
61.2.4 (e)
47.10.3 (d)
23.7.37 (a)
41.12.3 (r)
17.6.10 (c)
1.1.21 (y)
```

**Flag** - `byuctf{ilovedarcy}`