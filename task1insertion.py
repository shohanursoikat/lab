# Read from input1.txt
file = open("input1.txt", "r")

n = int(file.readline())

arr = list(map(int, file.readline().split()))

file.close()

# Insertion Sort

for i in range(1, n):

    key = arr[i]

    j = i - 1

    while j >= 0 and arr[j] > key:

        arr[j + 1] = arr[j]

        j -= 1

    arr[j + 1] = key

# Write to output1.txt
output = open("output1.txt", "w")

output.write(" ".join(map(str, arr)))

output.close()

print("Insertion Sort Completed")
