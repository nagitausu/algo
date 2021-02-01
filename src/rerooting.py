class Rerooting:
    def __init__(self, edge):
        self.n = len(edge)
        self.e = 0
        self.merge = lambda a, b : max(a, b)
        self.add_node = lambda v, index : v + 1
        self.ret = [self.e] * self.n
        self.dfs()
        self.dfs2()

    def dfs(self):
        st = [(-1, 0, 0)]
        while st:
            p, v, d = st.pop()
            if d == 0:
                if p != -1:
                    st.append((v, p, 1))
                for nv in edge[v]:
                    if nv == p:
                        continue
                    st.append((v, nv, 0))
            else:
                self.ret[v] = self.merge(self.ret[v], self.add_node(self.ret[p], p))
    
    def dfs2(self):
        st = [(-1, 0)]
        root_ret = self.ret[0]
        self.ret[0] = self.e
        while st:
            p, v = st.pop()
            for nv in edge[v]:
                if nv == p:
                    continue
                if p != -1:
                    self.ret[nv] = self.merge(self.ret[nv], self.add_node(self.ret[v], v))
                st.append((v, nv))
        self.ret[0] = self.merge(self.ret[0], root_ret)

if __name__ == "__main__":
    edge = [[1], [0, 2, 3], [1, 4, 5], [1, 6, 7], [2], [2], [3], [3]]
    RR = Rerooting(edge)
    print(RR.ret)