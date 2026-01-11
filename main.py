import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# ==========================================
# ЗАВДАННЯ 1: Створення та аналіз графа
# ==========================================
print("\n>>> ЗАВДАННЯ 1: Створення та візуалізація графа")

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (частини міста)
nodes = ["Центр", "Північ", "Південь", "Захід", "Схід", "Вокзал", "Аеропорт", "Парк", "Ринок", "Університет"]
G.add_nodes_from(nodes)

# Додавання ребер (маршрутів)
edges = [
    ("Центр", "Вокзал"), ("Центр", "Університет"), ("Центр", "Парк"),
    ("Вокзал", "Північ"), ("Вокзал", "Захід"),
    ("Північ", "Аеропорт"), ("Північ", "Ринок"),
    ("Захід", "Парк"), ("Захід", "Аеропорт"),
    ("Парк", "Південь"),
    ("Південь", "Ринок"), ("Південь", "Схід"),
    ("Схід", "Університет"),
    ("Університет", "Ринок")
]
G.add_edges_from(edges)

# Аналіз характеристик
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print("\nСтупені вершин (кількість зв'язків):")
for node, degree in G.degree():
    print(f"  {node}: {degree}")

# Візуалізація
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=2000, font_size=10, font_weight='bold', edge_color='gray')
plt.title("Транспортна мережа міста (Завдання 1)")
print("\n[INFO] Графік відкрито у новому вікні. Закрийте його, щоб продовжити виконання програми.")
plt.show()


# ==========================================
# ЗАВДАННЯ 2: DFS і BFS
# ==========================================
print("\n>>> ЗАВДАННЯ 2: Пошук шляхів (DFS та BFS)")

def dfs_path(graph, start, goal):
    """Пошук у глибину (Depth-First Search)"""
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_node in set(graph.neighbors(vertex)) - set(path):
            if next_node == goal:
                return path + [next_node]
            stack.append((next_node, path + [next_node]))
    return None

def bfs_path(graph, start, goal):
    """Пошук у ширину (Breadth-First Search)"""
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next_node in set(graph.neighbors(vertex)) - set(path):
            if next_node == goal:
                return path + [next_node]
            queue.append((next_node, path + [next_node]))
    return None

# Вибір точок маршруту
start_node = "Аеропорт"
end_node = "Університет"

# Запуск алгоритмів
dfs_result = dfs_path(G, start_node, end_node)
bfs_result = bfs_path(G, start_node, end_node)

print(f"Маршрут від '{start_node}' до '{end_node}':")
print(f"  DFS (глибина): {dfs_result}")
print(f"  BFS (ширина):  {bfs_result}")

print("\n[Аналіз різниці]")
print("DFS часто знаходить довший, звивистий шлях, бо йде до кінця в одну сторону.")
print("BFS у незваженому графі завжди знаходить найкоротший шлях за кількістю ребер.")


# ==========================================
# ЗАВДАННЯ 3: Алгоритм Дейкстри
# ==========================================
print("\n>>> ЗАВДАННЯ 3: Алгоритм Дейкстри")

# Додаємо ваги до ребер (відстань/час)
# Вага = час у хвилинах або відстань у км
weighted_edges = [
    ("Центр", "Вокзал", 2), ("Центр", "Університет", 5), ("Центр", "Парк", 4),
    ("Вокзал", "Північ", 6), ("Вокзал", "Захід", 3),
    ("Північ", "Аеропорт", 10), ("Північ", "Ринок", 4),
    ("Захід", "Парк", 3), ("Захід", "Аеропорт", 8),
    ("Парк", "Південь", 5),
    ("Південь", "Ринок", 2), ("Південь", "Схід", 3),
    ("Схід", "Університет", 4),
    ("Університет", "Ринок", 3)
]

# Оновлюємо граф вагами
G.add_weighted_edges_from(weighted_edges)

# Знаходження найкоротшого шляху за допомогою бібліотечної функції
dijkstra_path = nx.dijkstra_path(G, start_node, end_node, weight='weight')
dijkstra_length = nx.dijkstra_path_length(G, start_node, end_node, weight='weight')

print(f"Найкоротший шлях (Дейкстра) від '{start_node}' до '{end_node}':")
print(f"  Шлях: {dijkstra_path}")
print(f"  Сумарна вага (довжина/час): {dijkstra_length}")