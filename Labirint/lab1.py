from collections import deque

graf = {
    'A': ['M', 'P'],
    'M': ['A', 'N'],
    'P': ['A', 'B'],
    'N': ['M', 'B'],
    'B': ['N', 'P']
}


def dkstr(start, goal, graph):
    queue = deque([start])
    visidet = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visidet:
                queue.append(next_node)
                visidet[next_node] = cur_node
    return visidet


start = 'A'
goal = 'N'
visidet = dkstr(start, goal, graf)
print(visidet)

# cur_node = goal
# print(f'path from{goal} to {start}: \n {goal}', end='')
# while cur_node != start:
#     cur_node = visidet[cur_node]
#     print(f'---> {cur_node}', end='')
