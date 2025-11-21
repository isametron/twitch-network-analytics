"""Visualization module for network analysis results."""

import matplotlib.pyplot as plt
import networkx as nx


def plot_network(graph, title="Network Graph"):
    """
    Plot the network graph.
    
    Args:
        graph: NetworkX graph object
        title: Title for the plot
    """
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=300, node_color='lightblue')
    nx.draw_networkx_edges(graph, pos, alpha=0.5)
    nx.draw_networkx_labels(graph, pos, font_size=10)
    plt.title(title)
    plt.axis('off')
    plt.show()


def plot_centrality_distribution(centrality_scores, title="Centrality Distribution"):
    """
    Plot centrality score distribution.
    
    Args:
        centrality_scores: Dictionary of centrality scores
        title: Title for the plot
    """
    plt.figure(figsize=(10, 6))
    plt.bar(centrality_scores.keys(), centrality_scores.values())
    plt.title(title)
    plt.xlabel('Node')
    plt.ylabel('Centrality Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
