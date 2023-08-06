# solution to the code studio question

def printAdjacency(n, m, edges):
    # Write your code here.
    
    adj_list = [None] * n

    for edge in edges:
        u, v = edge
        if adj_list[u] is None:
            adj_list[u] = list()
            adj_list[u].append(u)
        adj_list[u].append(v)
        if adj_list[v] is None:
            adj_list[v] = list()
            adj_list[v].append(v)
        adj_list[v].append(u)

    return adj_list

    pass

# try uncommenting the following lines of code and runnning the file

# adj_lists = printAdjacency(4, 3, [[1, 2], [0, 3], [2, 3]])
# for adj_list in adj_lists:
#     print(*adj_list)

'''
expected output:
0 3  
1 2  
2 1 3
3 0 2
'''