def findMax(list) :
    max = list[0]
    for i in range (1, len(list)) :
        if max < list[i] :
            max = list[i]
    return max

numbers = [5, 2, 9, 8, 1, 4, 7, 3, 6]
max = findMax(numbers)
print(max)