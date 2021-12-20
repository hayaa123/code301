from graph.graph import Graph

def is_direct (graph , arr):
    weight = 0 
    for i in range (len(arr)-1):
         starting_point  = arr[i]
         distination = arr[i+1]
         graph_nodes = graph.get_nodes() 
         for node in graph_nodes :
            if node.value == starting_point:
                starting_point = node  
            if node.value == arr[i+1]:
                distination = node
         if distination not in [edge.vertix for edge in graph.get_edge(starting_point)]:
               print([edge.vertix for edge in graph.get_edge(starting_point)])
               return [False, "0$"]
         for edge in graph.get_edge(starting_point) : 
               if distination == edge.vertix :
                    weight += edge.weight
                    break 
    return [True, f"{weight}$"] 