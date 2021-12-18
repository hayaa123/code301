from graph.graph import Graph,Vertix,Edge
import pytest

# Node can be successfully added to the graph
def test_add_node():
    graph = Graph()
    graph.add_node(4)
    actual = graph._graph_list
    assert len(actual.keys()) == 1  


# An edge can be successfully added to the graph

def test_add_edge():
    graph = Graph()
    node1= graph.add_node(4)
    node2= graph.add_node(6)
    graph.add_edge(node1,node2)
    assert isinstance(graph._graph_list[node1][0],Edge)

# A collection of all nodes can be properly retrieved from the graph

def test_get_all_nodes_in_graph(graph):
    actual = set(graph[0].get_nodes())
    expected = {graph[1],graph[2],graph[3]}
    assert actual == expected

# All appropriate neighbors can be retrieved from the graph

def test_get_all_neighbors_in_graph(graph):
    the_graph =graph[0]
    node1 = graph[1]
    node2= graph[2]
    node3 = graph[3]
    actual = the_graph.get_edge(node1)
    assert len(actual) ==2  and isinstance(actual[0],Edge) and isinstance(actual[0],Edge)

# Neighbors are returned with the weight between nodes included

def test_get_all_neighbors_with_weight_in_graph(graph):
    the_graph =graph[0]
    node1 = graph[1]
    node2= graph[2]
    node3 = graph[3]
    actual = the_graph.get_edge(node1)[0].weight
    expected = None
    assert expected==actual


# The proper size is returned, representing the number of nodes in the graph

def test_get_size_in_graph(graph):
    the_graph =graph[0]
    actual = the_graph.size()
    expected = 3
    assert expected==actual

# A graph with only one node and edge can be properly returned
def test_get_node():
    graph = Graph()
    node =graph.add_node(4)
    actual = set(graph.get_nodes())
    expected = {node}
    assert actual == expected

# An empty graph properly returns null
def test_get_empty():
    graph = Graph()
    actual = set(graph.get_nodes())
    expected = set()
    assert actual == expected



@pytest.fixture
def graph():
    graph = Graph()
    node1= graph.add_node(3)
    node2=graph.add_node(4)
    node3= graph.add_node(5)
    graph.add_edge(node1,node2)
    graph.add_edge(node2,node3)
    graph.add_edge(node1,node3)

    return graph ,node1,node2,node3