from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.directed = False

    def __str__(self):
        graph_string = ''
        for node, neighbour in self.adj_list.items():
            graph_string += f'{node} -> {neighbour}\n'
        return graph_string
    
    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError('Node already exist')
        
    def remove_node(self, node):
        if node not in self.adj_list:
            raise ValueError('Node does not exist')
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
            self.adj_list[from_node].add((to_node,weight))
            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def remove_edge(self, from_node, to_node):
        if from_node in self.adjacency_lst:
            if to_node in self.adjacency_lst[from_node]:
                self.adjacency_lst[from_node].remove(to_node)
            else:
                raise ValueError('Edge does not exist')
            if not self.directed:
                if from_node in self.adjacency_lst[to_node]:
                    self.adjacency_lst[to_node].remove(from_node)
        else:
            raise ValueError('Edge does not exist')


    def get_neighbours(self, node):
        return self.adj_list.get(node, set())
    

    def breadth_first_search(self, start):
        visited = set()
        queue = deque([start])
        bfs = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                bfs.append(node)
                neighbours = self.get_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        queue.append(neighbour)
        return bfs

    def depth_first_search(self, start):
        visited = set()
        stack = [start]
        dfs = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                dfs.append(node)
                neighbours = self.get_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                     stack.append(neighbour)
        return dfs


if __name__ == '__main__':
    g = Graph()
    g.add_node(10)
    g.add_edge(10,11,3)
    g.add_edge(11,12,4)
    print(g)
    print(g.breadth_first_search(10))
    print(g.depth_first_search(10))