
from utils import path_from_dfs
from utils import bfs, encode, gen_adjacency_matrix, matrix_to_list,dfs,rev_path
import time
import sys

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


t = dfs(matrix_to_list(y),0,34)

path = rev_path(t,0,34)

pas = path_from_dfs(path, 0, 34)
for i in range(len(pas)+1):
    tmp = pas[0:i]
    res = ""
    for i in range(len(maze)):
        for j in range(len(maze)):
            if [i,j] in encoded["pos"]:
                if encoded["pos"].index([i,j]) in tmp:
                    res+="+"
                else:
                    res+=" "
            else:
                res+="#"
        res+="\n"
    print(res)
    time.sleep(1)
    sys.stdout.write('\x1b[10A')
sys.stdout.write('\x1b[10B')
        





