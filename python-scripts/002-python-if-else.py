# solution for challenge: 002 - Python If-Else
# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

# The variable n = 24 below is just a sample for test, remove it if you want to use on Hacker Rank
n = 24

if n % 2 != 0:
    print('Weird')
else:
    if n > 20:
        print('Not Weird')
    elif n >= 2 and n <= 5:
        print('Not Weird')
    elif n >= 6 and n <= 20:
        print('Weird')
