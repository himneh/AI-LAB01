import numpy as np


def DFS(matrix, start, end):
    """
    BFS algorithm:
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
    print(path) 
    print(visited) 
   

    return visited, path



def BFS(matrix, start, end):
    """
    DFS algorithm
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
    print(path) 
    print(visited) 
   
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
    # TODO:  
    path=[]
    visited={}
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
        fx = [matrix[open[i]][end] for i in range(len(open))]
        pos = fx.index(min(fx))
        curr = open.pop(pos)
        close.append(curr)
        temp = False
        #if find end node:
        if curr == end:
            break
        for index in range(size):
            if index not in close and index not in open and matrix[curr][index] == 1:                           
                open.append(index)
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

    print(visited)
    print(path)
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
    # TODO: 
    path=[]
    visited={}

    return visited, path

