from utils import bfs, encode, gen_adjacency_matrix, matrix_to_list 


from typing import List


maze:"List[List[str]]" = []
maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])


encoded = encode(maze)
y = gen_adjacency_matrix(maze=encoded["enc"],pos_list=encoded["pos"])


t = bfs(matrix_to_list(y),0,len(encoded["pos"])-1)

res = ""
for i in range(len(maze)):
    for j in range(len(maze)):
        if [i,j] in encoded["pos"]:
            if encoded["pos"].index([i,j]) in t:
                res+="+"
            else:
                res+="O"
        else:
            res+="#"
    res+="\n"
print(res)
        




