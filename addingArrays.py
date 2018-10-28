N = input("How many elements in each array?  ")

numArray1 = list(map(int, input("Enter elements of array 1: ").split()))
numArray2 = list(map(int, input("Enter elements of array 2: ").split()))

sumArray = []

for i, j in zip(numArray1, numArray2):
    sumArray.append(i+j)

for element in sumArray:
    print(element, end=' ')
