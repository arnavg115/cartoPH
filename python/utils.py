from typing import  List


def encode(maze:"List[List[str]]"):
    encoded_maze:"List[List[int]]" = []
    inc = 0
    pos_list:"List[List[int]]" = []
    for index,line in enumerate(maze):
        nl = []
        for ind, char in enumerate(line):
            if char == "#":
                nl.append(-1)
            else:
                nl.append(inc)
                pos_list.append([index, ind])
                inc+=1

        encoded_maze.append(nl)
    return {"enc":encoded_maze,"pos":pos_list}

def gen_adjacency_matrix(maze:"List[List[int]]",pos_list:"List[List[int]]") -> "List[List[int]]":
    adds = [[-1,0],[1,0],[0,1],[0,-1]]
    matrix = []
    for i in range(len(pos_list)):
        u = []
        for i in range(len(pos_list)):
            u.append(0)
        matrix.append(u)
    
    for index,node in enumerate(pos_list):
        for ls in adds:
            if [node[0]+ls[0],node[1]+ls[1]] in pos_list and [node[0]+ls[0],node[1]+ls[1]] != node:
                matrix[index][pos_list.index([node[0]+ls[0],node[1]+ls[1]])] = 1
        matrix[index][index] = 0

            
    return matrix

def print_array(array):
    res = ""
    for line in array:
        for obj in line:
            res+=f"|{str(obj)}|"
        res+="\n"
    print(res)

def bfs(graph,start:int, end:int):
    # credit for this code goes to https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
    # pls check it out
    visited = []
    queue = [[start]]

    while len(queue) > 0:
        curr = queue.pop(0)
        node = curr[-1]
        if node not in visited:
            surrounders = graph[node]

            for surrounder in surrounders:
                new = list(curr)
                new.append(surrounder)
                queue.append(new)
                if surrounder == end:
                    return new
    return "Problems"


def matrix_to_list(matrix):
    # credit to this code goes to https://stackoverflow.com/a/43377477
    graph = {}
    for i, node in enumerate(matrix):
        adj = []
        for j, connected in enumerate(node):
            if connected:
                adj.append(j)
        graph[i] = adj
    return graph

