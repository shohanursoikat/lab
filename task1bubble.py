# Read from input2.txt
file = open("input2.txt", "r")

n = int(file.readline())

arr = list(map(int, file.readline().split()))

file.close()

for i in range(n):

    swapped = False

    for j in range(0, n - i - 1):

        if arr[j] > arr[j + 1]:

            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            swapped = True

    # Stop early if already sorted
    if not swapped:
        break

# Write to output2.txt
output = open("output2.txt", "w")

output.write(" ".join(map(str, arr)))

output.close()

print("Bubble Sort Completed")
