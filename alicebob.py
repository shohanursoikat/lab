# Read input

with open("input3.txt", "r") as file:

    N = int(file.readline())

    arr1 = list(map(int, file.readline().split()))

    M = int(file.readline())

    arr2 = list(map(int, file.readline().split()))

# Combine arrays

merged = arr1 + arr2

# Sort combined array

merged.sort()

# Write output

with open("output3.txt", "w") as output:

    output.write(" ".join(map(str, merged)))

print("Work has been done")
