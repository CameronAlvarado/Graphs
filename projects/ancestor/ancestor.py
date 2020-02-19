from graph import Graph


def earliest_ancestor(ancestors, starting_node, nodes=None):
    # Create a graph
    if nodes is None:
        nodes = set()
    # instantiate a graph
    graph = Graph()
    # loop through array of tuples
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
        # Add edges from tuples BACKWARDS
        graph.add_edge(tuple[1], tuple[0])
    # print(graph.vertices)

    path_list = []
    lengths = []
    possible = []

    # find paths to every possible vertex
    for vertex in nodes:
        earliest = graph.dfs_recursive(starting_node, vertex)
        if earliest is not None:
            path_list.append(earliest)
    # print(path_list)

    # Create list of the lengths of possible paths
    for arr in path_list:
        lengths.append(len(arr))
    # print(lengths)

    # Find the longest path
    longest = max(lengths)
    # print(longest)
    for path in path_list:
        if len(path) is longest:
            # Return -1 if only possible path is the same
            if path[-1] is starting_node:
                return(-1)
            else:
                # Append possible ends to array
                possible.append(path[-1])
                # Grab the least of possible ends.
                smallest = min(possible)
                return(smallest)
