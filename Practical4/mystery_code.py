# What does this piece of code do?
# Answer: The code can find a random prime number between 1 and 100.

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
#-jeff: for integer, it won't change
from math import ceil

p=False
while p==False:#the loop is controlled by Boolean variables
    p=True
    n = randint(1,100)#randomly get a integer between 1 and 100
    u = ceil(n**(0.5))#take square root and the ceiling of n, assigned to u
    for i in range(2,u+1):
        if n%i == 0:
            p=False
        #if we can find factors of n between 2 and u+1, choose another n
        #if the n has no factor between 2 and u+1

print(n)
            
