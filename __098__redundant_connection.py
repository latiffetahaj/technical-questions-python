'''
    684. Redundant Connection
    In this problem, a tree is an undirected graph that is connected and has no cycles.

    You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
    The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
    The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

    Return an edge that can be removed so that the resulting graph is a tree of n nodes.
    If there are multiple answers, return the answer that occurs last in the input.

    Constraints:
        n == edges.length
        3 <= n <= 1000
        edges[i].length == 2
        1 <= ai < bi <= edges.length
        ai != bi
        There are no repeated edges.
        The given graph is connected.


    #LeetCode: https://leetcode.com/problems/redundant-connection/

    The Union Find uses Path Compression and union by rank so it's time complexity is very close to O(1).
    Precisely it is O(α(n)), where α(n) is the inverse Ackermann function.
    For practical purposes, α(n) can be considered almost constant (i.e., very close to O(1)).

    Time Complexity: n * O(1) = O(n)
    Space Complexity: O(n)
'''
# This algorithm uses an UNION-FIND (Disjoint Set) data structure.
# In this case it is used for cycle detection.
# As soon as a cycle is detected, return that edge that caused the cycle.
def find_redundant_connection(edges):
    parent = {}
    rank = {}
    n = len(edges)

    for i in range(1, n + 1):
        parent[i] = i
        rank[i] = 0

    for n1, n2 in edges:
        if not union(n1, n2, parent, rank):
            return [n1, n2]

def find(n, parent):
    p = parent[n]

    # Loop until the root parent is found.
    while p != parent[p]:
        parent[p] = parent[parent[p]] # Path Compression.
        p = parent[p]

    return p

def union(n1, n2, parent, rank):
    p1 = find(n1, parent)
    p2 = find(n2, parent)

    # Cycle detection, these components are already connected.
    if p1 == p2:
        return False

    if rank[p1] > rank[p2]:
        parent[p2] = p1
    elif rank[p2] > rank[p1]:
        parent[p1] = p2
    else:
        parent[p2] = p1
        rank[p1] += 1
    return True