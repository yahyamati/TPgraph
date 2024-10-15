import networkx as nx
from collections import deque

def parcours_en_largeur(graphe, sommet_depart):
    # Dictionary to store the shortest distance from sommet_depart to each node
    distance = {node: float('inf') for node in graphe.nodes()}
    distance[sommet_depart] = 0  # Distance to self is 0
    
    # Queue to handle the BFS
    queue = deque([sommet_depart])
    
    # BFS traversal
    while queue:
        current_node = queue.popleft()  # Dequeue a node from the front of the queue
        
        for neighbor in graphe.neighbors(current_node):
            # If neighbor hasn't been visited, or has a larger distance, update it
            if distance[neighbor] == float('inf'):  # If it hasn't been visited yet
                distance[neighbor] = distance[current_node] + 1
                queue.append(neighbor)  # Enqueue the neighbor
                
    # Return both the shortest distances and all nodes traversed
    return distance;
