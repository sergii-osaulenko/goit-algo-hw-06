from collections import deque

# Реалізація DFS (ітеративний підхід)
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_node in set(graph.neighbors(vertex)) - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                stack.append((next_node, path + [next_node]))

# Реалізація BFS (ітеративний підхід)
def bfs_paths(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next_node in set(graph.neighbors(vertex)) - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))

# Використання алгоритмів
start_node = "Аеропорт"
end_node = "Університет"

print(f"\nШляхи від {start_node} до {end_node}:")

# Отримуємо перший знайдений шлях для DFS
dfs_result = list(dfs_paths(G, start_node, end_node))
print(f"DFS шлях: {dfs_result[0] if dfs_result else 'Не знайдено'}")

# Отримуємо перший знайдений шлях для BFS
bfs_result = list(bfs_paths(G, start_node, end_node))
print(f"BFS шлях: {bfs_result[0] if bfs_result else 'Не знайдено'}")