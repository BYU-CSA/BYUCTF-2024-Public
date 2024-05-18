# Who Ami I
Description:
```markdown
We have a Word file placed on one of our machines by a cyber attacker. Who is the author of the document? 

Flag format - `byuctf{Author Name}`

[Who Am I.docx]
```

## Writeup
This challenge is an easy challenge designed to remind a user to look for document metadata whenever it is available. The author of the document can be found by using something like Exiftool, or it can be found by manually extracting the Word document and looking for it.

There are multiple ways to solve this challenge. Perhaps the most straightforward is by using Exiftool. Take the `Who Am I.docx` file, drag it onto Exiftool (or use the command line version), and copy the author name from there.

**Flag** - `byuctf{Ryan Sketchy}`