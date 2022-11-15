#Quiz 1, Question 2, Data Structures, UnB 2022.2
#Program to inform if it's possible to turn a string into a palindrome by changing one character
#Input: one string of 100 characteres
#Output: POSSIBLE or IMPOSSIBLE

import os

os.system('cls')

counter = 0

#getting string
word = input()

#convert it into a list
word = list(word)

y = len(word) - 1

#compare it with it backwards
for x in range(0, len(word) - 1):
    if word[x] != word[y]:
        counter = counter + 1
    y = y - 1

#output
if (counter <= 2 and len(word) % 2 != 0) or ((counter == 1 or counter == 2) and len(word) % 2 == 0):
    print("POSSIBLE")
    
else:
    print("IMPOSSIBLE")
