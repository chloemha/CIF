CIF Junior
---
Introduction
---
Coding Is Fun (CIF) is an organization that offers virtual classes to teach students python. There are three levels: beginner, junior, and senior. In every class, there are teachers that share their knowledge, and guide students through the different steps. There are also many peers to share ideas and learn with together. It is a friendly learning process that can help with future aspirations.

CIF Junior classes cover the following:
-  Python
-  Markdown
-  Mermaid
-  C++
-  Html
-  Javascript

and more!

In the duration of 20 units, with 20 classes, six projects are created by the students. 

Project 1
---
During classes two and three, we learned how to create number guessing games. The player would give the number range they wanted to guess in, and the system would randomly generate one. There are also hints that are given if the player is having a hard time.

Here is the flowchart of my number guessing game: 

``` mermaid
graph TD
  A[start] --> B[ask player for a number range] --> C[generate a random number based on given range] --> D[player guesses a number] --> E[do the numbers match?]
  E[do the numbers match?] --> F[you win!] --> L[end]
  E[do the numbers match?] --> G[you lose!]
  G[you lose!] --> H[hints: player's guess is too big/smalll, the number is even/odd] --> I[try again?]
  I[try again?] --> J[yes] --> D[player guesses a number]
  I[try again?] --> K[no] --> L[end]
```

You can also find my code of my number guessing game on my CIF repository under "unit 3". 

Other
---
more to come soon!

Links
---
CIF: https://www.itisfun.org/

Medium: https://medium.com/@chloe.m.ha
