from graph import Graph


def earliest_ancestor(ancestors, starting_node, nodes=None):
    # Use Depth First Search
    # ancestors is an array of tuples
    if nodes is None:
        nodes = set()
    # instantiate a graph
    graph = Graph()
    # loop through array of edges
    for tuple in ancestors:
        # add numbers to set of possible nodes
        if tuple[0] not in nodes:
            nodes.add(tuple[0])
        if tuple[1] not in nodes:
            nodes.add(tuple[1])
    # Add nodes as vertices
    for node in nodes:
        graph.add_vertex(node)
    for tuple in ancestors:
        # Add edges from tuples
        graph.add_edge(tuple[1], tuple[0])
    # print(graph.vertices)

    earliest = graph.dft(starting_node)
    print("earliest:", earliest)
    # if earliest is None:
    #     return -1
    # else:
    #     return earliest
