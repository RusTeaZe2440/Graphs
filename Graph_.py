from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = dict()
        self.directed = False

    def __str__(self):
        graph_str = ''
        for i, (nodes, neighbour) in enumerate(self.adj_list.items(),start=1):
            graph_str += f'{i} {nodes}->{neighbour}\n'
        return graph_str
    
    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            return 'node already exist'

    def remove_node(self, node):
        if node not in self.adj_list:
            return 'Node does not exist'
        for neighbour in self.adj_list.values():
            neighbour.discard(node)
        del self.adj_list[node]

    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)
        if weight is None:
            self.adj_list[from_node].add(to_node)
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node, weight))
            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def remove_edge(self, from_node, to_node):
        if from_node in self.adj_list and to_node in self.adj_list:  # Ensure both nodes exist
            if to_node in self.adj_list[from_node]:
                self.adj_list[from_node].remove(to_node)
            else:
                return 'Edge does not exist'

            if not self.directed:
                if from_node in self.adj_list[to_node]:  # Ensure from_node exists in to_node's list
                    self.adj_list[to_node].remove(from_node)
        else:
            return 'Edge does not exist'


    def get_neighbours(self, node):
        return self.adj_list.get(node, set())

    def get_nodes(self):
        return list(self.adj_list.keys())

    def has_node(self, node):
        return node in self.adj_list
    
    def has_edge(self, from_node, to_node):
        if from_node in self.adj_list:
            return to_node in self.adj_list[from_node]
        return False        
    
    def get_edges(self):
        edges = []
        for to_node in self.adj_list.values():
            edges.append(to_node)
        return edges
    
    def bfs(self, start):
        queue = deque([start])
        order = []
        visited = set()

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbours = self.get_neighbours(node)

                for neighbour in neighbours:
                    if neighbour not in visited:
                        neighbour = neighbour[0]
                        queue.append(neighbour)
        return order

    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)   
                order.append(node)
                neighbours = self.get_neighbours(node)

                for neighbour in neighbours:
                    if neighbour not in visited:
                        neighbour = neighbour[0]
                        stack.append(neighbour)
        return order


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'C', 2)
    g.add_edge('C', 'E', 4)
    g.add_edge('E','D', 3)
    g.add_edge('E','F', 5)
    g.add_edge('D', 'B', 8)
    print(g)
    print(g)
    print('Breadth-First-Search')
    print(g.bfs(0))
    print('Depth-First-Search')
    print(g.dfs(0))
    print('Edges')
    print(g.get_edges())
    print(g.get_nodes())
    print(g.remove_edge('A','B'))