from graph_business_trip.graph_business_trip import is_direct
import pytest

from graph.graph import Graph

def test_is_direct_for_a_and_B (graph):
    expected = [True , "5$"]
    actual = is_direct(graph,["A","B"])
    assert expected == actual

def test_A_and_C (graph):
    expected = [False , "0$"]
    actual = is_direct(graph,["A","C"])
    assert expected == actual

def test_E_And_F (graph):
    expected = [False , "0$"]
    actual = is_direct(graph,["E","F"])
    assert expected == actual


@pytest.fixture
def graph ():
    graph = Graph()
    node1=graph.add_node("A")
    node2=graph.add_node("B")
    node3= graph.add_node("C")
    node4 = graph.add_node("D")
    graph.add_edge(node1,node2,5)
    graph.add_edge(node2,node3,40)
    graph.add_edge(node3,node4,10)
    return graph



