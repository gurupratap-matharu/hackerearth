'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

s1 = list(input())
s2 = list(input())
difference = []

for elem in s1 + s2:
    if (elem not in s1 and elem not in s1):
        difference.append(elem)
print(len(difference))
