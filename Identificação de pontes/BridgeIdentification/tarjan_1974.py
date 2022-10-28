def tarjan(graph):
    low = disc = [float('inf')] * len(graph)
    pontes = list()
    time = iter(range(len(graph)))
    def search(u, p):
        low[u] = disc[u] = next(time)
        for v in graph[u]:
            if v == p: continue
            if not disc[v]:
                search(u, v)
                if disc[u] < low[v]:
                    pontes.append([u, v])
                    pontes.append([v, u])
                low[u] = min(low[u], low[v])
            else:
                low[u] = min(low[u], disc[v])
    for u in range(len(graph)):
        if not disc[u]:
            search(u, u)
    return pontes
