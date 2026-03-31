array = [90, 10, 20, 40, 60, 70, 80, 30, 50, 100]

print("Array before sort : ", array)
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print("Array after sorting : ", array)
