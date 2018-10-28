'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here


L = int(input())
N = int(input())

photosArray = []

for _ in range(N):
    photosArray.append(list(map(int, input().split())))

for photo in photosArray:
    length, width = photo

    if length < L or width < L:
        print("UPLOAD ANOTHER")
    elif length > L or width > L:
        print("CROP IT")
    else:
        print("ACCEPTED")
