# Cosmere
Description:
```markdown
Welcome to the cosmere! We recently discovered this online quiz that can tell us a lot about different orders of the Knights Radiant. On a scale of Free-spirited to Disciplined, what percent disciplined is the ideal Dustbringer? 

Flag format - `byuctf{percentage}` (ie, `byuctf{45}`)

https://www.brandonsanderson.com/official-knights-radiant-order-quiz/

*Please note, THIS IS NOT OUR WEBSITE. You cannot use automated tools of any kind. You don't have to script this one. Figure it out.*
```

maximum 5 attempts

## Writeup
The online quiz is written in JavaScript, which means that the whole thing happens client side. After doing some investigation into the code, you can discover that user inputs are compared to a three-dimensional array called `traitData`, which has the ideal slider positions for each order in each question. Further investigation will reveal that question 4 is missing from the HTML list of questions, but not the array. After playing around with this, you can discover that the disciplined vs free spirit question is question 15, and that the dustbringer traits are index 2 in the array. This means that ideal dustbringer is 87% disciplined. 

**Flag** - `byuctf{87}`