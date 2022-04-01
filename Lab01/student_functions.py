from http.client import CONTINUE
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
        path.append(curr)
        if(curr == end): break
        for index in range(size):
            if tmp[index] == False and matrix[curr][index] == 1:                           
                st.append(index)
                if(temp == False): visited[index] = curr
                if(end == index): temp = True
                tmp[index] == True


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
        path.append(curr)       

        if curr == end: break

        for index in range(size):
            if tmp[index] == False and matrix[curr][index] == 1:                           
                q.append(index)
                if(temp == False): visited[index] = curr
                if(end == index): temp = True
                tmp[index] == True
     
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
    # TODO: 
    path=[]
    visited={}
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

