# coding: utf-8
import random

def generate_tree(n, raw=False):
    nodes = [i for i in range(n)]
    random.shuffle(nodes)

    # Prepare tree edge
    group = []
    tree_edge = []
    for i in range(n):
        if i == 0:
            group.append(nodes[i])
            continue
        u = random.sample(group, 1)[0]
        v = nodes[i]
        if u > v:
            u, v = v, u
        tree_edge.append((v, u))
        group.append(nodes[i])

    if raw:
        return tree_edge
    else:
        tree_edge_list = [[] for _ in range(n)]
        for u, v in tree_edge:
            tree_edge_list[u].append(v)
            tree_edge_list[v].append(u)
        return tree_edge_list

def generate_simple_connected_graph(n, raw=False):
    # Prepare simple connected graph edge
    tree_edge = generate_tree(n, raw=True)
    edge_set = set(tree_edge)
    all_edge = [(i, j) for i in range(n) for j in range(i, n)]
    edge_set = edge_set.union(random.sample(all_edge, n//3))
    simple_connected_edge = list(edge_set)

    if raw:
        return simple_connected_edge
    else:
        simple_connected_edge_list = [[] for _ in range(n)]
        for u, v in simple_connected_edge:
            simple_connected_edge_list[u].append(v)
            simple_connected_edge_list[v].append(u)
        return simple_connected_edge_list