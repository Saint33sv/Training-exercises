import sys


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        """Этот метод обеспечивает симметричность графика. Если есть путь А к В со значением V, должен быть
        путь В к А со значением V."""

        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
        return graph

    def get_nodes(self):
        """Возвращает узлы графа"""
        return self.nodes

    def get_outgoing_edges(self, node):
        """Возвращает соседей узла"""
        connection = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connection.append(out_node)
        return connection

    def value(self, node1, node2):
        """Возвращает значение ребра между узлами"""
        return self.graph[node1][node2]


shortest_path = {}
previouns_nodes = {}


def dijkstra_algoritm(graph, start_node):
    unvisidet_nodes = list(graph.get_nodes())
    max_value = sys.maxsize
    for node in unvisidet_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0
    """Алгоритм исполняется до тех пор пока не посетит все узлы."""
    while unvisidet_nodes:
        """Код ниже находит узел с найменьшей оценкой"""
        current_min_node = None
        for node in unvisidet_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        """Приведенный код ниже извлекает соседей текущего узла и обновляет их расстояния"""
        neighbors = graph.get_outgoing_edges(current_min_node)  # Соседи текущего узла
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                """Обновление лучшего пути к текущему узлу"""
                previouns_nodes[neighbor] = current_min_node
        """После посещения соседей текущего узла отмечаем его как пройденый"""
        unvisidet_nodes.remove(current_min_node)


def print_result(previons_node, shortes_path, start_node, target_node):
    path = []
    node = target_node
    while node != start_node:
        path.append(node)
        node = previons_node[node]
    """Добавим начальный узел вручную"""
    path.append(start_node)
    print(f"Найден лучший маршрут с ценостью {shortes_path[target_node]}")


nodes = ['Reykjavik', 'Oslo', 'Moscow', 'London', 'Rome', 'Berlin', 'Belgrade', 'Athens']
init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph['Reykjavik']['Oslo'] = 5
init_graph['Reykjavik']['London'] = 4
init_graph['Oslo']['Berlin'] = 1
init_graph['Oslo']['Moscow'] = 3
init_graph['Moscow']['Belgrade'] = 5
init_graph['Moscow']['Athens'] = 4
init_graph['Athens']['Belgrade'] = 1
init_graph['Rome']['Berlin'] = 2
init_graph['Rome']['Athens'] = 2


graph = Graph(nodes, init_graph)

# dijkstra_algoritm(graph, start_node='Reykjavik')
# print_result(previons_node=previouns_nodes, shortes_path=shortest_path, start_node='Reykjavik', target_node='Moscow')

print(graph.construct_graph(nodes=nodes, init_graph=init_graph))
