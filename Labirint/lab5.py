from collections import deque


matrix = [[0, 5, 4, 0, 0, 0, 0, 0],
          [5, 0, 0, 1, 3, 0, 0, 0],
          [4, 0, 0, 3, 0, 0, 0, 0],
          [0, 1, 3, 0, 0, 0, 2, 9],
          [0, 3, 0, 0, 0, 4, 0, 5],
          [0, 0, 0, 0, 4, 0, 2, 1],
          [0, 0, 0, 2, 0, 2, 0, 0],
          [0, 0, 0, 9, 5, 1, 0, 0]]


class DijkstaAloritm(object):

    def __init__(self, matrix, start_node, finish_node):
        self.matrix = matrix
        self.start = start_node - 1
        self.finish = finish_node - 1
        self.S = {}
        self.visidet = {}

    def soedi(self, node):
        s = {}
        for index, value in enumerate(self.matrix[node]):
            if value > 0:
                s[index] = value
        return s

    def dcstr(self):
        queue = deque([self.start])
        self.S[self.start] = 0
        while queue:
            cur_node = queue.popleft()
            for sosed in self.soedi(cur_node):
                if sosed not in self.S or self.S[cur_node] + self.matrix[cur_node][sosed] < self.S[sosed]:
                    self.S[sosed] = self.S[cur_node] + self.matrix[cur_node][sosed]
                    self.visidet[sosed] = cur_node
                    queue.append(sosed)

        path = []
        node = self.finish
        while node != self.start:
            path.append(str(node+1))
            node = self.visidet[node]
        path.append(str(self.start+1))
        print(f'Найден новый путь с длиной {self.S[self.finish]}')
        print('--->'.join(reversed(path)))


d = DijkstaAloritm(matrix, 1, 8)
d.dcstr()



