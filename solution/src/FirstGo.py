'''
Solving the hackerrank Anagram puzzle

https://www.hackerrank.com/challenges/anagram

---------------------

Problem Statement

Sid is obsessed with reading short stories. Being a CS student, he is doing some interesting frequency analysis with the books. He chooses strings S1 and S2 in such a way that |len(S1)-len(S2)|<=1.

Your task is to help him find the minimum number of characters of the first string he needs to change to enable him to make it an anagram of the second string.

Note: A word x is an anagram of another word y if we can produce y by rearranging the letters of x.

Input Format 
The first line will contain an integer, T, representing the number of test cases. Each test case will contain a string having length len(S1)+len(S2), which will be concatenation of both the strings described above in the problem.The given string will contain only characters from a to z.

Output Format 
An integer corresponding to each test case is printed in a different line, i.e. the number of changes required for each test case. Print -1 if it is not possible.

Constraints

1<=T<=100 
1<=len(S1)+len(S2)<=104

---------------------

Created on 1 Jan 2016

@author: chris
'''
from collections import Counter

for _ in range(input()):
    inputString = raw_input().strip()
    
    output = -1
    if not len(inputString)%2:
        left = inputString[:len(inputString)/2]
        right = inputString[len(inputString)/2:]
        
        leftCounts  = Counter(left)
        rightCounts = Counter(right)
        output = sum((leftCounts - rightCounts).values())
    
    print output
        
    