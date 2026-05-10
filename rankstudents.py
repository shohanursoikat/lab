# Read input using with open()

with open("input2.txt", "r") as file:

    n = int(file.readline())

    ids = list(map(int, file.readline().split()))

    marks = list(map(int, file.readline().split()))

# Selection Sort

for i in range(n):

    max_index = i

    for j in range(i + 1, n):

        # Higher marks get priority
        if marks[j] > marks[max_index]:

            max_index = j

        # If marks are same,
        # smaller ID gets priority
        elif marks[j] == marks[max_index]:

            if ids[j] < ids[max_index]:

                max_index = j

    # Swap marks
    marks[i], marks[max_index] = marks[max_index], marks[i]

    # Swap ids
    ids[i], ids[max_index] = ids[max_index], ids[i]

# Write output using with open()

with open("output2.txt", "w") as output:

    for i in range(n):

        output.write(
            "ID: " + str(ids[i]) +
            " Mark: " + str(marks[i]) + "\n"
        )

    output.write("\nWork has been done")

print("Work has been done")
