import networkx as nx
import numpy as np
import plotly.graph_objects as go
from Bfs_algorithm import parcours_en_largeur  # Import the function

# Create a NetworkX graph (undirected)
G = nx.Graph()

def add_node():
    node = input("Enter node name: ")
    G.add_node(node)
    print(f"Node '{node}' added successfully!")

def add_edge():
    node1 = input("Enter first node: ")
    node2 = input("Enter second node: ")
    edgename = input("Enter Name of Edge: ")
    
    if node1 in G.nodes and node2 in G.nodes:
        G.add_edge(node1, node2, name=edgename)
        print(f"Edge {edgename} between '{node1}' and '{node2}' added successfully!")
    else:
        print("Both nodes must exist in the graph! Add the nodes first.")
        
def display_adjacency_matrix():
    
    if len(G.nodes) == 0:
        print("The graph has no nodes yet. Add nodes first!")
        return
    
    print("Displaying adjacency matrix of the graph...")

    # Get the adjacency matrix as a NumPy array
    adj_matrix = nx.to_numpy_array(G)
    
    # Display the adjacency matrix with labeled nodes
    nodes = list(G.nodes)
    print("\nAdjacency Matrix:")
    
    # Print the header row (node labels)
    print("   " + "  ".join(nodes))
    
    # Print each row of the adjacency matrix with the corresponding node label
    for i, row in enumerate(adj_matrix):
        print(f"{nodes[i]}: " + "  ".join(map(str, row.astype(int))))

def display_graph():
    print("Displaying interactive graph in browser...")

    # Generate a layout for the graph
    pos = nx.spring_layout(G)

    # Extract positions for edges
    edge_x = []
    edge_y = []
    edge_text = []
    
    for edge in G.edges(data=True):
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)
        edge_name = edge[2].get('name', 'Unnamed')
        edge_text.append(f"Edge: {edge_name} between {edge[0]} and {edge[1]}")

    # Edge trace (lines between nodes)
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='#888'),
        hoverinfo='text',
        text=edge_text,
        mode='lines')

    # Extract positions for nodes
    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    # Node trace (node markers)
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            size=20,
            line_width=2),
        text=[f"Node {node}" for node in G.nodes()])  # Hover text for each node

    # Plotly graph with edges and nodes, no extra UI, zoom/pan enabled
    fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='Graph non oriente',
                showlegend=False,
                hovermode='closest',
                margin=dict(b=0, l=0, r=0, t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                dragmode='pan',  # Enables dragging and panning
                ))

    fig.show()

def interface():
    while True:
        print("\nMenu:")
        print("1. Add Node")
        print("2. Add Edge")
        print("3. Display Matrix Adj ")
        print("4. Display Graph")
        print("5. Perform BFS")
        print("6. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            add_node()
        elif choice == '2':
            add_edge()
        elif choice == '3':
            display_adjacency_matrix()
        elif choice == '4':
            display_graph()
        elif choice == '5':
            start_node = input("Enter the start node for BFS: ")
            if start_node in G.nodes:
                distances = parcours_en_largeur(G, start_node)
                print(f"Shortest distances between {start_node} and other nodes:")
                for node, dist in distances.items():
                    print(f"distance between {start_node} and {node} is: {dist}")
               
            else:
                print(f"Node '{start_node}' does not exist in the graph.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    interface()
