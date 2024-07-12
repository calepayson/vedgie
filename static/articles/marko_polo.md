# Marko Polo

### Marko Polo?

Ya, it's not the most informative title but cest la vie (hopefully that roughly translates to I don't really care as I'm expecting all of three people to read this (Hi Mom)). 

Marko Polo is a quote generator I wrote in C which immedeately begs two questions. In the age of ChatGPT why would I build a worse quote generator and, given the urge to build something useless, why build it in C a language that everyone from my C professor to the president agrees is *not* the language you want to use when starting a new project?

Let's start with why I chose C... Simple, I enjoy it. 

I'm largely self taught which has advantages and disadvantages that are mostly summarized by the the statement "I read the entire textbook and did most of the exercises". In case the advantage of that statement isn't obvious, in my experience the vast majority of university students don't open their textbook, let alone read it.

The disadvantage of that statement is much more pernicious. See, when you're self taught, there are no extrinsic constraints. There is nothing to prevent you from going too deep or too broad on a topic, no one to say, "You could learn more but you're hitting a point of diminishing returns".You are your own mentor.

## I love C because of its simplicity

There's really no point in going deeper than C. I'm sure there are plenty of wonderful reasons to become fluent in assembly but I get the sense there's no need. Save it for later in your career when you're chasing incremental improvement. With C you're as close to the metal as you *need* to be. 

C is a very small language. Seriously, no youtube click bait here, you could get very very good at it in a couple of weeks. Why? It has nearly no features. Hell you can't even do objects. The textbook is less than 190 pages! That's insane! I just got "Python for Data Analysis" and the sections on pandas and NumPy come out to just under 400 pages and those are just libraries! (ok, maybe a bit of a disengenuis comparison but if you're in the weeds enough to call me on it then you know how simple C is).

C has a tiny standard library. This goes hand in hand with being a small language but is worth speaking of on its own. In higher level programming languages I always get caught trying to figure out whether to write my own function or find an abstraction. This is an advantage for those langagues in most cases. DRY, right? If someone else has written in, just use that. But for folks who are self taught and curious, this is a field of landmines. That lack of constraint means I'll spend an hour diving into a library instead of writing code. Or looking for a library instead of writing code. I'll read all the docs and try exercises to make sure I have a good handle on this library before I implement it. And then I'll never use it again. Why am I like this?

With C, finding the right abstraction isn't an issue. Because it probably doesn't exist. Spend a day reading through the C standard library (it might not even take a day), and next time you're wondering whether to implement it yourself or not, go implement it yourself you sweet prince (I'm all for feminine subjects but the majority of engineers are dudes and I'm also all for realism).

### Markov Chains are Simple

After taking just about every lower division CS course that UCSC offers at once, I felt I had a good handle on writing code but had no intuition for building a project. I assume this is the point of the upper division courses but oh well, I'm too poor for those. I went to my favorite professor and asked him what textbooks, courses, etc. he would recommend to understand projects and, to my shock, he said there weren't any. 

He said the only way to learn how to structure projects is through trial and error. There's no grand strategy, just philosophy and intuition. 

So my goal right now is to slam away at personal projects, mostly to maximize my fuckups. This isn't a fail fast situation in the standard sense where you make mistakes until the customer rewards you. No, this is some form of goal-oriented masocism. I'm aiming to make *every* mistake to build up an intuition for solutions.

When I was helping build the Database at InnerPlant our data was screwed up. It was unstandardized, repetitive, and stored across multiple google sheets. At the time I knew something was wrong with that but I didn't know what. When I discovered relational databases it felt like a salve, like I had been dipped in holy water. I fell in love with relational databases becuase it made the pain go away.

In essence, if mistakes are scars I want to look like batman so that I have an intuition for things that *just work*. When I come across new technologies do they poke at a tender place or do they soothe it. Is it added complexity or is it a real solution. 

I chose the Markov Chain because I'm interested in ML and Markove Chains seem like the simplest form. I want practice implementing data structures and algorithms and I want to make simple mistakes. Mistakes that are my fault, not some dependency hell like you can get from abstractions. 

For the most part it worked. 

My first iteration quickly got out of hand. I tried to split it out "like a pro", to modularize it like all the cool projects on github and quickly ran into the complexity monster. I spent so much time making abstractions in project strucure that by the time I sat down to code I was lost. 

Learning: Always start with the base case. It's easier to refactor something that works than to build it perfect from scratch.

My second attempt also fell prey to complexity. This time I opened up main.c, started coding away, and within a few hours I was hopelessly lost again. 

Learning: Make small plans. My first mistake was planning too much, my second was not planning at all. There's a middle ground that seems right for exploring the problem space. 

I decided to plan small units. I would plan each data structure and its methods in a design doc, write them in an unoptomized way, and repeat with the next data structure. Inevitably I had to add and refactor functions along the way, and I did so without concerning myself with performance. After ensuring that everything worked and the project did in fact spit out quotes, I went back through and refactored/documented each part. After each refactor I would run the program again and again until I was certain it workd.

Learning: Write tests. Maybe it doesn't have to be the full TDD approach, something that always feels slow and overly complex when you're learning. But, after that first pass, you should write tests to cover all aspects of your code so that when you refactor, you don't have to hand run your program 30 different ways. Just run the tests.

### Overall

I have a long way to go before I'm a great engineer, and I suspect I'll never be one of the best because of my late start, but this project felt like a big milestone. When you're self-taught it's hard to compare yourself to your peers (at least it is for me because I don't know any). I vacilate between God and Inferiority complexs throughout the week and this felt like a wonderful temper on that. I'm no programming genius but I can implement a project from scratch. That seems significant.
