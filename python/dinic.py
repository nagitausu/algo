from collections import deque
INF = 10**9

class Dinic:
    def __init__(self, n):
        self.n = n
        self.edge = [[] for _ in range(n)]
        self.level = [None] * self.n 
        self.it = [None] * self.n 

    def add_edge(self, fr, to, cap):
        # edge consists of [dest, cap, id of reverse edge]
        forward = [to, cap, None]
        backward = [fr, 0, forward]
        forward[2] = backward
        self.edge[fr].append(forward)
        self.edge[to].append(backward)

    def add_bidirect_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge2 = [v1, cap2, edge1]
        edge1[2] = edge2
        self.edge[v1].append(edge1)
        self.edge[v2].append(edge2)

    # takes start node and terminal node
    # create new self.level, return you can flow more or not 
    def bfs(self, s, t):
        self.level = [None] * self.n
        dq = deque([s])
        self.level[s] = 0
        while dq:
            v = dq.popleft()
            lv = self.level[v] + 1
            for dest, cap, _ in self.edge[v]: 
                if cap > 0 and self.level[dest] is None:
                    self.level[dest] = lv
                    dq.append(dest)
        return self.level[t] is not None

    # takes vertex, terminal, flow in vertex
    def dfs(self, v, t, f):
        if v == t:
            return f
        for e in self.it[v]:
            to, cap, rev = e
            if cap and self.level[v] < self.level[to]:
                ret = self.dfs(to, t, min(f, cap))
                # find flow
                if ret:
                    e[1] -= ret
                    rev[1] += ret
                    return ret
        # no more flow
        return 0

    def flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            for i in range(self.n):
                self.it[i] = iter(self.edge[i])
            # *self.it, = map(iter, self.edge)
            f = INF
            while f > 0:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

if __name__ == "__main__":
    # sample from URL below
    # https://www.slideshare.net/hcpc_hokudai/flow-cut
    DNC = Dinic(6)        
    DNC.add_edge(0, 1, 10)
    DNC.add_edge(0, 2, 4)
    DNC.add_edge(1, 3, 9)
    DNC.add_edge(1, 4, 6)
    DNC.add_edge(2, 4, 3)
    DNC.add_edge(4, 5, 4)
    DNC.add_edge(3, 5, 8)
    DNC.add_edge(2, 5, 3)

    flow = DNC.flow(0, 5)
    print(flow)