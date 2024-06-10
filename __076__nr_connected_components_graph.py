'''
    Count Connected Components
    There is an undirected graph with n nodes.
    There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.
    Return the total number of connected components in that graph.

    Constraints:
        1 <= numCourses <= 2000
        0 <= prerequisites.length <= 5000
        prerequisites[i].length == 2
        0 <= ai, bi < numCourses
        All the pairs prerequisites[i] are unique.

    #LeetCode: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

    Time Complexity: O(V + E)

    Space Complexity: O(V + E)
'''
# The algorithm follows a simple DFS.
# As we visit each node using DFS, we mark them as visited.
# Call the DFS on unvisited nodes, and each time increment count by 1.

def count_components(n, edges):
    count = 0
    adj = {}
    visited = set()
    for i in range(n):
        adj[i] = []

    for src, dst in edges:
        adj[src].append(dst)
        adj[dst].append(src)

    for i in range(n):
        if i not in visited:
            dfs(i, adj, visited)
            count += 1

    return count



def dfs(node, adj, visited):
    if node in visited:
        return

    visited.add(node)

    for n in adj[node]:
        dfs(n, adj, visited)

    return