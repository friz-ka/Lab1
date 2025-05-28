import math

def dijkstra(graph, start_v):
    """
    Скрипт реализует алгоритм Дейкстры для поиска кратчайших путей от произвольной начальной вершины до всех остальных.
    :param graph: матрица смежности
    :param start_v: индекс начальной вершины
    :return: два списка:
        - dist: кратчайшие расстояния до каждой вершины
        - prev: предыдущие вершины на кратчайшем пути
    """
    num_v = len(graph)
    dist = [math.inf] * num_v  # расстояния до вершин
    prev = [None] * num_v     # предыдущие вершины в путях
    visited = [False] * num_v # посещенные вершины

    dist[start_v] = 0

    for _ in range(num_v):  # выбираем не посещённую вершину с минимальным расстоянием
        min_dist = math.inf
        u = None
        for v in range(num_v):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v

        if u is None:
            break  # все оставшиеся вершины недостижимы

        visited[u] = True

        # обновляем расстояния для смежных вершин
        for v in range(num_v):
            if graph[u][v] != 0 and not visited[v]:
                alt = dist[u] + graph[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    return dist, prev

def reconstruct_path(prev, start, end):
    """
    Восстановить путь из одной вершины start в целевую end по списку prev.
    :param start: начальная вершина
    :param end: целевая вершина
    :param prev: список предыдущих вершин
    :return: список вершин пути или пустой список, если путь не существует
    """
    path = []
    at = end
    while at is not None:
        path.append(at)
        at = prev[at]
    path.reverse()
    
    if path[0] == start:
        return path
    else:
        return []

# Пример использования:

# Граф в виде матрицы смежности (0 — отсутствие ребра)
graph = [
    [0, 7, 9, 0, 0, 15],          # вершина 0
    [7, 0, 10, 17, 0, 0],         # вершина 1
    [9, 10, 0, 4, 0, 2],          # вершина 2
    [0, 17, 4, 0, 6, 0],          # вершина 3
    [0, 0, 0, 6, 0, 9],           # вершина 4
    [15, 0, 2, 0, 9, 0]           # вершина 5
]

start_v = 2

distances, previous = dijkstra(graph, start_v)

# Путь до всех вершин
for v in range(len(graph)):
    end_v = v
    path = reconstruct_path(previous, start_v, end_v)
    print(f"Самый короткий путь от {start_v} до {end_v}: {path}")