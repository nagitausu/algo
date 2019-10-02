import sys
sys.setrecursionlimit(10**6)
from collections import deque

class DirectedGraph:
    def __init__(self, adj):
        self.n = len(adj)
        self.adj = adj
        self.is_asyclic = False
        self.max_path_len = None

    def reverse_adj(self):
        self.reverse_adj = [[] for _ in range(self.n)]
        for u, vs in enumerate(self.adj):
            for v in vs:
                self.reverse_adj[v].append(u)

    def topological_sort(self):
        indegree = [0] * self.n
        for i, vs in enumerate(self.adj):
            for dest in vs:
                indegree[dest] += 1
        zero_v = []
        for v, indeg in enumerate(indegree):
            if indeg == 0:
                zero_v.append(v)
        max_path_len = 1
        tp_sorted = []
        to_be_added = []
        while True:
            while zero_v:
                v = zero_v.pop()
                tp_sorted.append(v)
                for dest in self.adj[v]:
                    indegree[dest] -= 1
                    if indegree[dest] == 0:
                        to_be_added.append(dest)
            if len(to_be_added) > 0:
                zero_v.extend(to_be_added)
                to_be_added = []
                max_path_len += 1
            else:
                break
        if len(tp_sorted) == self.n:
            self.is_asyclic = True
            self.max_path_len = max_path_len
            return tp_sorted
        else:
            self.is_asyclic = False
            return None

    def extract_cycle(self):
        seen = [0] * self.n
        checked = [0] * self.n
        hist = deque()
        self.node_in_cycle = -1

        self.reverse_adj()

        def dfs(v):
            seen[v] = 1
            hist.append(v)
            for nv in self.adj[v]:
                if checked[nv]:
                    continue
                if seen[nv] and not checked[nv]:
                    self.node_in_cycle = nv
                    return
                dfs(nv)
                if self.node_in_cycle != -1:
                    return
            hist.pop()
            checked[v] = 1

        for i in range(self.n):
            if not checked[i]:
                dfs(i)
            if self.node_in_cycle != -1:
                break
        if self.node_in_cycle == -1:
            self.is_asyclic = True
            return []
        else:
            self.is_asyclic = False
            cycle = []
            while hist:
                t = hist.pop()
                cycle.append(t)
                if t == self.node_in_cycle:
                    break
            cycle.reverse()
            return cycle

    def strongly_connected_components_decomp(self):
        visited = [0] * self.n
        order = []
        self.comp = [-1] * self.n

        def dfs(v):
            if visited[v]:
                return
            visited[v] = 1
            for nv in self.adj[v]:
                dfs(nv)
            order.append(v)

        def rdfs(v, cnt):
            if self.comp[v] != -1:
                return
            self.comp[v] = cnt
            for nv in self.reverse_adj[v]:
                rdfs(nv, cnt)

        for i in range(self.n):
            dfs(i)
        order.reverse()

        components_num = 0
        for v in order:
            if self.comp[v] == -1:
                rdfs(v, components_num)
                components_num += 1

        scc = [[] for _ in range(components_num)]
        for u in range(self.n):
            for v in self.adj[u]:
                if self.comp[u] == self.comp[v]:
                    continue
                scc[self.comp[u]].append(self.comp[v])
        return scc



if __name__ == "__main__":
    n = 8
    edge = [[] for _ in range(n)]
    edge[0].append(1)
    edge[1].append(2)
    edge[2].append(3)
    edge[3].append(0)
    edge[5].append(6)
    edge[5].append(1)
    edge[6].append(2)
    edge[2].append(7)
    edge[7].append(4)
    # edge[8].append(9)

    DG = DirectedGraph(edge)
    tp_sorted = DG.topological_sort()
    print("topological sort")
    print(tp_sorted)
    print(DG.max_path_len)

    cycle = DG.extract_cycle()
    print("extrace cycle")
    print(cycle)
    scc = DG.strongly_connected_components_decomp()
    print("strongly connected components")
    print(scc)
    print(DG.comp)
