class DirectedGraph:
    def __init__(self, adj):
        self.n = len(adj)
        self.adj = adj
        self.is_asyclic = False
        self.max_path_len = None

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
                zero_v += to_be_added
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

if __name__ == "__main__":
    n = 8
    edge = [[] for _ in range(n)]
    edge[0].append(1)
    edge[1].append(2)
    edge[2].append(3)
    edge[3].append(4)
    edge[5].append(6)
    edge[5].append(1)
    edge[6].append(2)
    edge[2].append(7)
    edge[7].append(4)
    # edge[8].append(9)

    DG = DirectedGraph(edge)
    tp_sorted = DG.topological_sort()
    print(tp_sorted)
    print(DG.max_path_len)
