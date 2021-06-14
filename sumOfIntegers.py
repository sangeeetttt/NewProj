'''
9. Write a python program to find sum of the first n positive integers.
sum = (n*(n+1))/2
'''
print(f'To find the sum of integers up to nth term,')
first = int(input('Enter the value of n: '))

sum = (first*(first+1))/2
print(f'the sum of integers up to {first} is {sum}')