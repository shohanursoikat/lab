# Read from input1.txt
file = open("input1.txt", "r")

n = int(file.readline())

arr = list(map(int, file.readline().split()))

file.close()

# Selection Sort

for i in range(n):

    min_index = i

    for j in range(i + 1, n):

        if arr[j] < arr[min_index]:

            min_index = j

    # Swap
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Write to output1.txt
output = open("output1.txt", "w")

output.write(" ".join(map(str, arr)))

output.close()

print("Selection Sort Completed")
