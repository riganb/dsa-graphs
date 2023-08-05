class Graph:
    def __init__(self, is_directed: bool) -> None:
        self.__is_directed = is_directed
        self.__adjacency_list = dict()
    
    def add_edge(self, u, v):
        if u not in self.__adjacency_list:
            self.__adjacency_list[u] = list()
        
        self.__adjacency_list[u].append(v)

        if not self.__is_directed:
            if v not in self.__adjacency_list:
                self.__adjacency_list[v] = list()

            self.__adjacency_list[v].append(u)
    
    def print_adjacency_list(self):
        for node, adj_list in self.__adjacency_list.items():
            print(f'{node}: {", ".join(map(str, adj_list))}')

n = int(input("Enter the number of nodes: "))
m = int(input("Enter the number of edges: "))

# change it to True for a directed graph
graph = Graph(False)

print('Enter the edges separated by newlines, and a space between the 2 nodes on each line:')

for i in range(m):
    graph.add_edge(*map(int, input().split()))

graph.print_adjacency_list()

'''
Sample input:
5
6
0 1
1 2
2 3
3 4
0 4
1 3

Expected output:
0: 1, 4
1: 0, 2, 3
2: 1, 3
3: 2, 4, 1
4: 3, 0
'''