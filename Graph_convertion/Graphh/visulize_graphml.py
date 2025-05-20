import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graphml_file):
    """
    Visualize a graph from a graphml file.`
    
    Args:
        graphml_file: Path to the graphml file.
    """
    # Read the graphml file
    G = nx.read_graphml(graphml_file)
    
    # Draw the graph
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    
    # Show the plot
    plt.show()

# Example usage
graphml_file = r"C:\Users\smtgo\3D_STEP_Classification\Datasets\datasets\Graph_models\0\0_3.graphml"
graphml_file_ = r"C:\Users\smtgo\3D_STEP_Classification\Datasets\datasets\Graph_models\0\0_5.graphml"
visualize_graph(graphml_file)
visualize_graph(graphml_file_)