array = [100, 90, 80, 70, 30, 50]
n = len(array)
for i in range(int(n/2)):
    array[i], array[n-i-1] = array[n-i-1], array[i]

print(array)