"""Centrality analysis module."""

import networkx as nx


def calculate_degree_centrality(graph):
    """
    Calculate degree centrality for all nodes.
    
    Args:
        graph: NetworkX graph object
        
    Returns:
        dict: Centrality scores
    """
    return nx.degree_centrality(graph)


def calculate_betweenness_centrality(graph):
    """
    Calculate betweenness centrality for all nodes.
    
    Args:
        graph: NetworkX graph object
        
    Returns:
        dict: Centrality scores
    """
    return nx.betweenness_centrality(graph)


def calculate_closeness_centrality(graph):
    """
    Calculate closeness centrality for all nodes.
    
    Args:
        graph: NetworkX graph object
        
    Returns:
        dict: Centrality scores
    """
    return nx.closeness_centrality(graph)


def calculate_eigenvector_centrality(graph):
    """
    Calculate eigenvector centrality for all nodes.
    
    Args:
        graph: NetworkX graph object
        
    Returns:
        dict: Centrality scores
    """
    return nx.eigenvector_centrality(graph)
