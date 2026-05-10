from collections import deque

# Read input

with open("input6.txt", "r") as file:

    N, M, D = map(int, file.readline().split())

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

distance = [-1] * (N + 1)

parent = [-1] * (N + 1)

queue = deque()

# Start from city 1

start = 1

visited[start] = True

distance[start] = 0

queue.append(start)

while queue:

    node = queue.popleft()

    for neighbor in graph[node]:

        if not visited[neighbor]:

            visited[neighbor] = True

            distance[neighbor] = distance[node] + 1

            parent[neighbor] = node

            queue.append(neighbor)

# Reconstruct path

path = []

current = D

while current != -1:

    path.append(current)

    current = parent[current]

# Reverse path

path.reverse()

# Write output

with open("output6.txt", "w") as output:

    output.write("Time: " + str(distance[D]) + "\n")

    output.write("Shortest Path: ")

    output.write(" ".join(map(str, path)))

print("Shortest Path Found")
