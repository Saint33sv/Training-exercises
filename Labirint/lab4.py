import sys

nodes = ['Reykjavik', 'Oslo', 'Moscow', 'London', 'Rome', 'Berlin', 'Belgrade', 'Athens']
init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph['Reykjavik']['Oslo'] = 5
init_graph['Reykjavik']['London'] = 4
init_graph['Oslo']['Berlin'] = 1
init_graph['Oslo']['Moscow'] = 3
init_graph['Oslo']['Reykjavik'] = 5
init_graph['Moscow']['Belgrade'] = 5
init_graph['Moscow']['Athens'] = 4
init_graph['Moscow']['Oslo'] = 3
init_graph['Athens']['Belgrade'] = 1
init_graph['Athens']['Rome'] = 2
init_graph['Athens']['Moscow'] = 4
init_graph['Rome']['Berlin'] = 2
init_graph['Rome']['Athens'] = 2
init_graph['Belgrade']['Athens'] = 1
init_graph['Belgrade']['Berlin'] = 9
init_graph['Belgrade']['Moscow'] = 5
init_graph['Berlin']['Belgrade'] = 9
init_graph['Berlin']['Rome'] = 2
init_graph['Berlin']['Oslo'] = 1
init_graph['Berlin']['London'] = 3
init_graph['London']['Berlin'] = 3
init_graph['London']['Reykjavik'] = 4

shortest_path = {}
previons_nodes = {}

def dkstr(graph, start):
    unvisidet_nodes = nodes  # Создаем список не посещенных узлов
    max_value = sys.maxsize  # Создаем переменную со значением бесконечности
    for node in unvisidet_nodes:  # Проходим список всех не посещенных узлов
        shortest_path[node] = max_value  # Присваиваем всем узлам значение бесконечности
    shortest_path[start] = 0  # Устанавливаем стартовый узел и присваиваем ему нулевое значение
    while unvisidet_nodes:  # В цыкле пока список узлов не пуст
        cur_node = None  # Создаем переменную текущего Минимального узла со значением None
        for node in unvisidet_nodes:  # Проходим список всех не посещенных узлов
            if cur_node == None:  # 1-вое Условие если текущий узел без значения
                cur_node = node  # Присваиваем ему значение узла из списка(привязываем переменную к списку узлов)
            elif shortest_path[node] < shortest_path[cur_node]:  # Условие2 если значение узла из цыкла меньше чем значение переменной текущего узла
                cur_node = node  # Присваеваем переменной минимальное значение(тоесть стартового узла)
        sosedi = graph[cur_node]  # Переменная соседи это все узлы которые сопряжены с текущем узлом
        for sosed in sosedi:  # Перебераем соседей узла
            tentative_value = shortest_path[cur_node] + graph[cur_node][sosed]  # Предворительное значение ребра между узлом и соседом
            if tentative_value < shortest_path[sosed]:  # Условие если Предворительное значение меньше чем значение в словаре значений
                shortest_path[sosed] = tentative_value  # словарь подновляется минимальным значением
                previons_nodes[sosed] = cur_node  # Создаем словарь где ключ это сосед а значение это текущий узел
        unvisidet_nodes.remove(cur_node)  # Со списка узлов удаляем текущий узел (отмечаем его как пройденый)

def print_result(short_path, nodes, start, finish):
    pash = []
    node = finish
    while node != start:
        pash.append(node)
        node = nodes[node]
    pash.append(start)
    print(f'Найден новый путь с длиной {short_path[finish]}')
    print("-->".join(reversed(pash)))


dkstr(init_graph, 'Reykjavik')
print_result(shortest_path, previons_nodes, 'Reykjavik', 'Belgrade')






