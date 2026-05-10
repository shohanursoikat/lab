# Read input

with open("input5.txt", "r") as file:

    N, M = map(int, file.readline().split())

    # Create adjacency list

    graph = []

    for i in range(N + 1):

        graph.append([])

    # Read edges

    for i in range(M):

        u, v = map(int, file.readline().split())

        # Undirected graph
        graph[u].append(v)
        graph[v].append(u)

# DFS

visited = [False] * (N + 1)

stack = []

start = 1

stack.append(start)

result = []

while stack:

    node = stack.pop()

    if not visited[node]:

        visited[node] = True

        result.append(node)

        # Reverse needed for natural DFS order
        for neighbor in reversed(graph[node]):

            if not visited[neighbor]:

                stack.append(neighbor)

# Write output

with open("output5.txt", "w") as output:

    output.write(" ".join(map(str, result)))

print("DFS Traversal Completed")
