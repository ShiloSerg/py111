from typing import Hashable, Mapping, Union
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges:
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(edge[0], edge[1])], connectionstyle="arc3,rad=0.2"
        )

    plt.show()  # plt.savefig()


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """

    draw_graph(g)

    visited_nodes = {node: False for node in g.nodes}
    total_coasts = {node: float('inf') for node in g.nodes}
    current_node = starting_node
    total_coasts[current_node] = 0

    for _ in range(len(g)):
        not_visited_total_coasts = {node: coast for node, coast in total_coasts.items() if not visited_nodes[node]}
        min_v = float('inf')
        for k, v in not_visited_total_coasts.items():
            if v < min_v:
                min_v = v
                current_node = k

        visited_nodes[current_node] = True

        for neighbour_node in g[current_node]:
            weight = g[current_node][neighbour_node]['weight']
            total_coasts[neighbour_node] = min(total_coasts[neighbour_node], total_coasts[current_node] + weight)

    print(g, starting_node)
    return total_coasts

# G = nx.DiGraph()
# G.add_nodes_from("ABCDEFG")
# G.add_weighted_edges_from([
#             ("A", "B", 1),
#             ("B", "C", 3),
#             ("C", "E", 4),
#             ("E", "F", 3),
#             ("B", "E", 8),
#             ("C", "D", 1),
#             ("D", "E", 2),
#             ("B", "D", 2),
#             ("G", "D", 1),
#             ("D", "A", 2),
#         ])
#
# dijkstra_algo(G, 'A')
