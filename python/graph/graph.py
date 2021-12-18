class Vertix :
    """
    building block for graph takes value as input 
    to instansiate a Vertix object 
    """
    def __init__(self,value):
        self.value = value

class Edge :
    """
    edge between tow node

    takes the end_vertix and weight 
    """
    def __init__(self,vertix,weight):
        self.vertix = vertix
        self.weight = weight 

class Graph:
    """
    class used to create a graph objects 
    """
    def __init__(self):
        self._graph_list = {}

    def add_node (self,value):
        """
        add node to the graph 
        
        input -> value 

        output ->the added node 
        """
        vertix = Vertix(value)
        self._graph_list[vertix] = []
        return vertix

    def add_edge (self,vertix_start,vertix_end,weight=None):
        """
        add edge to the graph 
        
        input -> starting vertix , ending vertix , weight (optional default = None) 

        output ->nothing 

        """
        if vertix_start not in self._graph_list.keys():
            raise Exception ("the starting vertix does not exist in the graph ")
        if vertix_end not in self._graph_list.keys():
            raise Exception ("the ending vertix does not exist in the graph")
        edge = Edge (vertix_end,weight)
        self._graph_list[vertix_start].append(edge)

    def get_nodes(self):
        """
        takes no input

        returns all the nodes in the graph 
        """
        return self._graph_list.keys()

    def get_edge (self,node):
        """
        takes node as an input 
        
        returns all the adjacent edges in the graph 
        """

        return self._graph_list.get(node,[])

    def size (self):
        """
        this method will return the number of nodes in the graph 
        """
        return len(self._graph_list.keys())