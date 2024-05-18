# Gitting Started
Description:
```markdown
A local hacker, TheITFirefly, who started up a blog to talk about his exploits in the tech world, has hidden a flag in the source code for his blog. Luckily, his source code is publicly available in a git repo. 

https://gitlab.com/TheITFirefly/tech-blog
```

## Writeup
From looking through all the files in the repo right now, it doesn't look like the flag is available. So I started thinking that maybe TheITFirefly have tried to delete the flag from the git repo. Unfortunately for him, git stores a version of every file changed with every commit, which can make it extremely difficult to remove information once it has been committed to a git repo. The `git log` command can be used to view information about commits in a git repo, and adding the `-p` flag lets you see exactly what in each file was changed by a commit. 

Knowing this, I put this script together really quick to solve the challenge:  
```bash
#!/bin/bash
git clone https://gitlab.com/TheITFirefly/tech-blog.git
cd tech-blog
git log -p | grep byuctf
```

**Flag** - `byuctf{g1t_gud!}`