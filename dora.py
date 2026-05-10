from collections import deque

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

# BFS

visited = [False] * (N + 1)

queue = deque()

# Start from city 1

start = 1

visited[start] = True

queue.append(start)

# Store traversal

result = []

while queue:

    node = queue.popleft()

    result.append(node)

    for neighbor in graph[node]:

        if not visited[neighbor]:

            visited[neighbor] = True

            queue.append(neighbor)

# Write output

with open("output5.txt", "w") as output:

    output.write(" ".join(map(str, result)))

print("BFS Traversal Completed")
