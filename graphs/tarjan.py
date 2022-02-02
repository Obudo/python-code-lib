class StronglyConnectedComponentsFinder:
    '''
    Uses Tarjan's Algorithm to find all strongly connected components.
    Requires: number of nodes, adjacency list written as a map of id
    and adjacent nodes.
    Explained by https://www.youtube.com/watch?v=wUgWX0nc4NY
    '''
    UNVISITED = -1

    def __init__(self, number_of_nodes, adjacency_map):
        self.n = number_of_nodes
        self.adjacents = adjacency_map
        self.seen_nodes = 0
        self.strongly_connected_components = []
        self.ids = [self.UNVISITED for _ in range(number_of_nodes)]
        self.low = [self.UNVISITED for _ in range(number_of_nodes)]
        self.on_stack = [False for _ in range(number_of_nodes)]
        self.stack = []

    def scc_tarjan(self):
        for i in range(self.n):
            if self.ids[i] == self.UNVISITED:
                self.__dfs(i)

    def __dfs(self, root_id):
        self.stack.append(root_id)
        self.on_stack[root_id] = True
        self.ids[root_id] = self.low[root_id] = self.seen_nodes
        self.seen_nodes += 1

        for neighbor_id in self.adjacents[root_id]:
            if self.ids[neighbor_id] == self.UNVISITED:
                self.__dfs(neighbor_id)
            if self.on_stack[neighbor_id]:
                self.low[root_id] = min(self.low[root_id], self.low[neighbor_id])

        if self.ids[root_id] == self.low[root_id]:
            self.__clear_stack(root_id)

    def __clear_stack(self, root_id):
        scc = []
        while True:
            node_id = self.stack.pop()
            self.on_stack[node_id] = False
            self.low[node_id] = self.ids[root_id]
            scc.append(node_id)
            if node_id == root_id:
                break
        self.strongly_connected_components.append(scc)


if __name__ == '__main__':
    n = 8
    adjs = {
        0: [1,2],
        1: [0, 3],
        2: [3],
        3: [4,5],
        4: [2, 5, 6],
        5: [7],
        6: [5],
        7: [6]
    }
    finder = StronglyConnectedComponentsFinder(n, adjs)
    finder.scc_tarjan()
    print(finder.strongly_connected_components)