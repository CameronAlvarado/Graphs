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

    path_list = []
    no_none = []
    ends = []
    for vertex in nodes:
        earliest = graph.dfs_recursive(starting_node, vertex)
        path_list.append(earliest)

    for path in path_list:
        if path is not None:
            no_none.append(path)
    print(no_none)

    for path in no_none:
        ends.append(path[-1])
    print(ends)

    # print("earliest:", earliest)
    # if earliest is None:
    #     return -1
    # else:
    #     return earliest
