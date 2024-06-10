'''
    Graph Valid Tree

    Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
    write a function to check whether these edges make up a valid tree.

    You can assume that no duplicate edges will appear in edges.
    Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

    Constraints:
        1 <= n <= 100
        0 <= edges.length <= n * (n - 1) / 2


    #LeetCode: https://leetcode.com/problems/graph-valid-tree/

    Time Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges.
    Space Complexity: O(V + E)
'''

# To determine if a given graph is a valid tree, we need to check:
# If there is any cycle, and if the graph is connected.
# To be a valid tree the graph needs to be connected and have no cycles.
# Determining cycles in an undirected graph is a bit tricky because we can detect false loops.
# For example in an undirected graph: 0 <---> 1 can be deteced as a false loop.
# To avoid this, when we do a DFS, we also send the prev-node as an argument to skip false loops.

def is_graph_valid_tree(n, edges):
    visited = set()
    path = set()

    # Build an adjecency list.
    adj = {}
    for i in range(n):
        adj[i] = []

    for src, dst in edges:
        adj[src].append(dst)
        adj[dst].append(src)

    # Checking len(visited) == n becauase in a connected graph, from any nodes with DFS, we can visit all other nodes.
    # prev_node initially is -1 because all nodes are with values from 0 to n-1.
    if dfs(0, -1, adj, visited, path) and len(visited) == n:
        return True
    else:
        return False


def dfs(node, prev_node, adj, visited, path):
    if node in path:
        return False

    if node in visited:
        return True

    visited.add(node)
    path.add(node)

    for n in adj[node]:
        if n == prev_node:
            continue
        if not dfs(n, node, adj, visited, path):
            return False

    path.remove(node)
    return True