import networkx as nx

from collections import deque
from heapq import heappush, heappop

def visit(g, source, enqueue, queuepop):
    n = source
    while True:
        enqueue(n, g[n])
        try:
            parent, n = queuepop()
        except IndexError:
            return
        yield parent, n

def enq_once(qextend, source):
    enqueued = set([source])
    print enqueued
    def enq(parent, children):
        print enqueued
        new = set(children) - enqueued
        qextend((n, child) for child in new)
        enqueued |= new
    return enq

def bfs(g, source):
    q = deque()
    return visit(g, source, enq_once(q.extend, source), q.popleft)

def dfs(g, source):
    q = []
    return visit(g, source, enq_once(q.extend, source), q.pop)

def dijkstra_visit(g, source, return_dists=False):
    queue = []
    dists = {source: 0}
    
    def enq(parent, adj):
        pdist = dists[parent]
        for child, dist in adj.items():
            if child in dists:
                continue
            heappush(queue, (pdist + dist, parent, child))
            
    def qpop():
        while True:
            dist, parent, child = heappop(queue)
            if child not in dists:
                dists[child] = dist
                return parent, child
            
    v = visit(g, source, enq, qpop)
    if return_dists:
        return v, dists
    return v

def astar_visit(g, source, target, heuristic=lambda u, v: 0,
                return_dists=False):
    queue = []
    dists = {source: 0}
    explored = set([source])
    
    def enq(parent, adj):
        pdist = dists[parent]
        for child, dist in adj.items():
            cdist = dist + pdist
            if dists.get(child, cdist + 1) < cdist:
                continue
            dists[child] = cdist
            heappush(queue, (cdist + heuristic(child, target), parent, child))

    def qpop():
        while True:
            _, parent, child = heappop(queue)
            if child not in explored:
                explored.add(child)
                return parent, child
            
    v = visit(g, source, enq, qpop)
    if return_dists:
        return v, dists
    return v

def astar_path(g, source, target, heuristic=lambda u, v: 0):
    paths = {source: [source]}
    for parent, child in astar_visit(g, source, target, heuristic):
        paths[child] = paths[parent] + [child]
        if child == target:
            return paths[child]
    raise nx.NetworkXError("None %s not reachable from %s" % (source, target))

def astar_path_length(g, source, target, heuristic=lambda u, v: 0):
    v, dists = astar_visit(g, source, target, heuristic, True)
    found = any(child == target for parent, child in v)
    if found:
        return dists[target]
    raise nx.NetworkXError("None %s not reachable from %s" % (source, target))

def dijkstra_path(g, source, target):
    paths = {source: [source]}
    for parent, child in dijkstra_visit(g, source):
        paths[child] = paths[parent] + [child]
        if child == target:
            return paths[child]
    raise nx.NetworkXError("None %s not reachable from %s" % (source, target))

def dijkstra_path_length(g, source, target):
    v, dists = dijkstra_visit(g, source, True)
    found = any(child == target for parent, child in v)
    if found:
        return dists[target]
    raise nx.NetworkXError("None %s not reachable from %s" % (source, target))

