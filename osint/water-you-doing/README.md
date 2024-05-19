# Water You Doing, Step-Eclipse?
Description:
```markdown
On April 7th, 2024 while visiting my parents, I took a walk to a local body of water. Sometime between 3:00PM and 3:30PM EST, I took some pictures of the scenery while sitting on a bench. Exactly 24 hours later, I took a picture of the Sun from the same bench.
Can you find the exact "what3words" location of the bench where I took the pictures?

Hint: https://what3words.com/

Flag format - `byuctf{first.second.third}`

[water.zip]
```

## Writeup
The intended solve involves finding a nice map of the eclipse that also includes local times. From there, you can determine roughly where in the US the pictures were taken (along the line of the eclipse from Illinois to Maine). I purposely chose a bad quality eclipse photo to emphasize the fact that the picture was taken under a total solar eclipse (100% totality). This line is much smaller across the US.  Looking at the pictures, you can find a few distinct features. 

First, there is a sign with the Hill dog food logo on it. The other main feature is that it is next to a large body of water.
If you look up Hill dog food locations, you will find that Hill only has two factories in the path of the eclipse. One in Indiana and one in Ohio. The one in Ohio doesn't have any large bodies of water near it, but the one in Indiana does. From there, you kinda just have to look around for a large body of water that has a pier like the image does. It's pretty distinct if you can visualize it. From there, the pictures match up with the left-most bench.

The solution is one of these squares: 
* https://what3words.com/mindset.keynote.dollars
* https://what3words.com/lately.nominations.manly

**Flag** - `byuctf{mindset.keynote.dollars}`, `byuctf{lately.nominations.manly}`