with open('67.txt') as file:
    text = file.read()

lines = text.strip().split('\n')
array = []
for line in lines:
    numbers = list(map(int, line.split()))
    array.append(numbers)

def biggestSum(array):
    lastLine = array[-1]
    penultimate = array[-2]
    for i in range(0, len(penultimate)):
        sum1 = lastLine[i] + penultimate[i]
        sum2 = lastLine[i+1] + penultimate[i]
        penultimate[i] = compare(sum1, sum2)
    array[-2] = penultimate
    array.pop()
    if len(array) == 1:
        print(array)
        return array
    else:
        biggestSum(array)

def compare(a, b):
    if a>b:
        return a
    else:
        return b

biggestSum(array)
print('hi')