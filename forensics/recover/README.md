# Not Sure I'll Recover From This
Description:
```markdown
You know, passwords arent easy for person of my age, it's pretty hard to remember my password, let alone my security questions! I can't login now, can you help a friend out and recover my security questions so I can login?

* Q1: What was your first pet's name?
* Q2: Where did your parents meet?
* Q3: What's the first name of your oldest cousin? 

Flag format - `byuctf{answer1_answer2_answer3}`

* Mirror 1 - https://byu.box.com/s/cy32j4ilnv50ncugyn0ue28ztfso1u4l
* Mirror 2 - https://drive.google.com/file/d/18-1ZT26FpTPEmxFyayXBtDpcbwEoSSDs/view?usp=sharing
```

## Writeup
Using the SAM registry hive you can view a users security questions in the `C:\Users\` folder.  

* Q1: What was your first pets name? - Jimothy  
* Q2: Where did your parents meet? - Idaho Falls  
* Q3: Whats the first name of your oldest cousin? - Zephanias  

**Flags**:
* `byuctf{jimothy_idaho_falls_zephanias}`
* `byuctf{jimothy_idaho falls_zephanias}`