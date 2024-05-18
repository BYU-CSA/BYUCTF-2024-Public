# Fake Smarties
Description:
```markdown
Can you exploit the issues in my Machine Learning Model?

`nc fakesmarties.chal.cyberjousting.com 1359`

[fake_smarties.zip]
```

## Writeup
The issue with this ML model lies in the math behind how it calculates confidence values. If you can get the model to determine a negative confidence value, or two very VERY low values, the math can make it output an overall confidence value of more than 100% (or less than -100%). Doing so will print the flag. 

The best method I've found has been to create your own wordlist from scraped reddit comments in order to figure out what words are not used. From there, you can craft a payload like below that will output a massive confidence value. 

Basically, you need to find a payload that is both different from any of the words in the training text, but also the words themselves need to be different in format and style than other words in the text. This is why a payload like "__9 9 9 9 9 9 9 9 9 9 9 9LLSO" will work, because the text doesn't often contain either the character "9" or a bunch of one letter words together. 
(possible payloads)

```markdown
deks 9
disk golf
flag
lightbox - (this one returns an insane value)
dog park
__9 9 9 9 9 9 9 9 9 9 9 9LLSO
```

NOTE: Due to how this model was originally trained, the same input might not always give the same output value. They should be similar, but part of the vulnerability is that a poorly trained AI model isn't consistent.

**Flag** - `byuctf{AI_1s_c00l_br0s}`

## Hosting
This challenge should be a Docker container that runs the script `script.py` on port 1359 each time a user connects. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```