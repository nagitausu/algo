# coding: utf-8
import random
random.seed(0)

import matplotlib.pyplot as plt
import networkx as nx

# Num of nodes should be <100 since it's too heavy
# <30 is better cause you cannot understand the graph more than that...
def plot(edge):
    nodes = list(set([item for pair in edge for item in pair]))
    g = nx.Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edge)

    plt.figure(figsize=(8,8))

    # Not to show axes
    plt.tick_params(labelbottom=False,
                    labelleft=False,
                    labelright=False,
                    labeltop=False)
    plt.tick_params(bottom=False,
                    left=False,
                    right=False,
                    top=False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)

    pos = nx.spring_layout(g, k=0.5, iterations=1000, seed=0)
    nx.draw_networkx_nodes(g, pos, node_color='b', edge_color="b" ,alpha=0.2)
    nx.draw_networkx_labels(g, pos, fontsize=14, font_weight="normal")
    nx.draw_networkx_edges(g, pos, alpha=0.4, edge_color='c')

    plt.tight_layout(True)
    plt.show()

if __name__ == "__main__":
    import graph_generator
    n = 30
    edge = graph_generator.generate_simple_connected_graph(n, raw=True)
    plot(edge)
