import networkx as nx
n = 25
p = 0.9
G = nx.erdos_renyi_graph(n, p)
a = 0
for i in G.nodes():
    a = a + G.degree(i)
print(f'Средняя степень вершин графа: {float(a)/len(G.nodes())}')
print(f'Средняя степень вершины графа по формуле: {(n-1)*p}')