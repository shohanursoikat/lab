# Read input

with open("input4.txt", "r") as file:

    N, M = map(int, file.readline().split())

    # Create adjacency matrix
    matrix = []

    for i in range(N + 1):

        row = []

        for j in range(N + 1):

            row.append(0)

        matrix.append(row)

    # Read edges

    for i in range(M):

        u, v, w = map(int, file.readline().split())

        matrix[u][v] = w

# Write output

with open("output4.txt", "w") as output:

    for i in range(N + 1):

        for j in range(N + 1):

            output.write(str(matrix[i][j]) + " ")

        output.write("\n")

print("Adjacency Matrix Created")
