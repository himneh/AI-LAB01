from dis import dis
from sys import maxsize
import numpy as np

from math import sqrt

def DFS(matrix, start, end):
    """
    DFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 
   
    path=[]
    visited={start:-1}

    size = len(matrix)

    tmp = [] #array check a node is visited or not?
    tmp = [False for i in range(size)] #init 

    # Initialize a stack of nodes and
    # push the starting node into it
    st = []
    st.append(start)
    tmp[start] = True
    temp = False

    while (len(st) > 0):
        # Pop the top 
        curr = st.pop()
        #path.append(curr)
        if(curr == end): break
        for index in range(size):
            if tmp[index] == False and matrix[curr][index] == 1:                           
                st.append(index)
                if(temp == False): visited[index] = curr
                if(end == index): temp = True
                tmp[index] = True

     #find path            
    res = end
    while res != start:      
        path.append(res)
        res = visited[res]

        # for i in visited:
        #     if i == res:
        #         res = visited[i]
    path.append(start)
    path.reverse()
    # print(path) 
    # print(visited) 
   

    return visited, path



def BFS(matrix, start, end):
    """
    BFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    path=[]
    visited={start:-1}

    size = len(matrix)

    tmp = [] #array check a node is visited or not?
    tmp = [False for i in range(size)] #init 

    # Initialize a queue of nodes and
    # push the starting node into it
    q = []
    q.append(start)
    tmp[start] = True
    temp = False

    while len(q) > 0:        
        curr = q.pop(0)    
        #path.append(curr)       

        if curr == end: break #check

        for index in range(size):
            if tmp[index] == False and matrix[curr][index] == 1:                           
                q.append(index)
                tmp[index] = True
                if(temp == False): visited[index] = curr #check if found end note, stop appending visited
                if(end == index): temp = True
    #find path            
    res = end
    while res != start:      
        path.append(res)

        for i in visited:
            if i == res:
                res = visited[i]
    path.append(res)
    path.reverse()
    # print(path) 
    # print(visited) 
   
    return visited, path


def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    """
    REFERENCES: https://www.educative.io/edpresso/what-is-uniform-cost-search
    https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/
    """

    # TODO:  
    path=[]
    visited={start:-1}   
    #init queue
    queue = []
    queue.append({'node': start, 'cost': 0})

    size = len(matrix) #size of matrix

    distance = [] #distance between start and nodes
    distance = [0 for i in range(size)] 

    tmp =[]  #checked array
    tmp = [False for i in range(size)] 

    temp = False   

    while len(queue) != 0:      
        #lay phan tu co distance nho nhat trong queue ra   
        min_distance = maxsize
        curr = -1
        for i in range(len(queue)):               
            if min_distance > queue[i]['cost']:
                min_distance = queue[i]['cost']
                curr = queue[i]['node']

        queue.remove({'node': curr, 'cost': min_distance})
               
        if (curr == end):
            break

        tmp[curr] = True

        for index in range(size):
            if (tmp[index] == False):
                if  matrix[curr][index] != 0:
                    distance[index] = matrix[curr][index] + distance[curr] 
                    visited[index] = curr                  
                    needAdd = True

                    #if node index exists at queue then erase it and re-add              
                    for j in range(len(queue)):                     
                        if index == queue[j]['node']:                                                      
                            if queue[j]['cost'] >= distance[index]:
                                queue.remove({'node': queue[j]['node'], 'cost': queue[j]['cost']})
                            else:
                                needAdd = False
                                                                                                                                     
                    if (needAdd == True):
                        queue.append({'node': index, 'cost': distance[index]})

    
    #find path
    ans = end  
    while ans != start:      
        path.append(ans)       
        for i in visited:
            if i == ans:              
                ans = visited[i]
                  
                                   
    path.append(ans)
    path.reverse()

    #handle special case: start adjacent to end
    res1 = 0
    for i in range(len(path) - 1):
        res1 = res1 + matrix[path[i]][path[i+1]]

    res2 = 0
    if matrix[start][end] != 0:
        res2 = matrix[start][end]
        if res2 < res1 :
            path = [start,end]
            visited[end] = start
        
    # print(path)
    # print(visited)
    return visited, path


def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    """
    REFERENCES: https://www.javatpoint.com/ai-informed-search-algorithms#:~:text=Greedy%20best%2Dfirst%20search%20algorithm,the%20advantages%20of%20both%20algorithms.
    """

    # TODO: 
    path=[]
    visited={start:-1}

    open = [] # QUEUE
    close = [] # VISITED QUEUE

    size = len(matrix) #size of matrix
    open.append(start)
    while len(open) > 0:
        #use heuristic
        fx = [matrix[open[i]][end] for i in range(len(open))]
        pos = fx.index(min(fx)) #find min
        curr = open.pop(pos)
        close.append(curr)
        temp = False
        #if find end node:
        if curr == end:
            break
        for index in range(size):
            if index not in close and index not in open and matrix[curr][index] != 0:                           
                open.append(index)
                if(temp == False): visited[index] = curr #check if found end node, stop appending visited
                if(end == index): temp = True
       
    #find path            
    res = end
    while res != start:      
        path.append(res)

        for i in visited:
            if i == res:
                res = visited[i]
    path.append(res)
    path.reverse()

    # print(visited)
    # print(path)
    return visited, path

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    """
    REFERENCES: https://www.stdio.vn/giai-thuat-lap-trinh/thuat-giai-a-DVnHj
    """

    # TODO: 
    path=[]
    visited={start:-1}
   
    
    open = [] # QUEUE
    close = [] # VISITED QUEUE

    size = len(matrix) #size of matrix
    open.append(start)

    distances = [] #distance between start and nodes
    distances = [0 for i in range(size)]
    
    while len(open) > 0:
        #use heuristic
        fx = []
        for i in range(len(open)):
            h = sqrt((pos[end][0] - pos[open[i]][0])**2 + (pos[end][1] - pos[open[i]][1])**2)
            g = distances[i]
            fx.append(h + g)
        poss = fx.index(min(fx)) #find min
        # print(fx)
        # print(poss)
        # print(open)
        curr = open.pop(poss)
        close.append(curr)
        temp = False
        #if find end node:
        if curr == end:
            break
        for index in range(size):
            if index not in close and index not in open and matrix[curr][index] != 0:                           
                open.append(index)
                distances[index] = matrix[curr][index] + distances[curr]
                if(temp == False): visited[index] = curr #check if found end node, stop appending visited
                if(end == index): temp = True
       
    #find path            
    res = end
    while res != start:      
        path.append(res)

        for i in visited:
            if i == res:
                res = visited[i]
    path.append(res)
    path.reverse()

    # print(visited)
    # print(path)
    
    return visited, path
