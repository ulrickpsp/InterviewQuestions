## SNAKE MOVEMENT

I found the following question in a recent interview so I'll post the code I used. </br>
It's not the exact question but the concept is the same. </br>
Feel free to suggest any improvement.

```

Given an array A of length M and with N being the lenght of each subarray calculate the amount of steps 
(starting at location 0,0) needed to complete the path, until a location is repeated.

A has the following format

A = [[".", ".", ".", ".", ".", "x", "x", "x"], 
     [".", "x", ".", ".", ".", "x", "x", "."], 
     [".", ".", ".", "x", "x", "x", "x", "x"]]

where every '.' means that the location is empty and a 'x' means that the location is occupied. 
The allowed steps are right, down, left, and up, always keeping that order. 
This means that if a right step cannot be done because location is occupied the next direction must be followed

For example, for the given A in the example the following steps are done:

[0, 1] [0, 2] [0, 3] [0, 4] [1, 4] [1, 3] [1, 2] [0, 2]

Once we reach location [0,2] the path has been completed as we already occupied that location before. 
So the amount of steps to repeat a location is 8

```



Same exercise is resolved in different ways:

* snake_simple_example: Fast way to solve it
* snake_classes_example: Nicer way to resolve it
