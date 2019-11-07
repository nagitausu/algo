# coding: utf-8
import random

def generate_tree(n, raw=False, cost=False):
    nodes = [i for i in range(n)]
    random.shuffle(nodes)

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
        if cost:
            c = random.randrange(1, n+1)
            tree_edge.append((u, v, c))
        else:
            tree_edge.append((u, v))
        group.append(nodes[i])

    if raw:
        return tree_edge
    else:
        tree_edge_list = [[] for _ in range(n)]
        if cost:
          for u, v, c in tree_edge:
              tree_edge_list[u].append((v, c))
              tree_edge_list[v].append((u, c))
        else:
          for u, v in tree_edge:
              tree_edge_list[u].append(v)
              tree_edge_list[v].append(u)
        return tree_edge_list

def generate_simple_connected_graph(n, density=1, raw=False):
    # Keep connectivity
    tree_edge = generate_tree(n, raw=True)
    edge_set = set(tree_edge)

    # Add edge node num * density times
    # If duplicated, edge disappears
    for i in range(int(n*density)):
        u = 0; v = 0
        while u == v:
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
        if u > v:
            u, v = v, u
        edge_set.add((u,v))
    simple_connected_edge = list(edge_set)

    if raw:
        return simple_connected_edge
    else:
        simple_connected_edge_list = [[] for _ in range(n)]
        for u, v in simple_connected_edge:
            simple_connected_edge_list[u].append(v)
            simple_connected_edge_list[v].append(u)
        return simple_connected_edge_list
