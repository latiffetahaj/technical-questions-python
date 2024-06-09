'''
    133. Clone Graph
    Given a reference of a node in a connected undirected graph.
    Return a deep copy (clone) of the graph.
    Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

    class Node {
            public int val;
            public List<Node> neighbors;
    }

    Constraints:
        The number of nodes in the graph is in the range [0, 100].
        1 <= Node.val <= 100
        Node.val is unique for each node.
        There are no repeated edges and no self-loops in the graph.
        The Graph is connected and all nodes can be visited starting from the given node.


    #LeetCode: https://leetcode.com/problems/clone-graph/

    Time Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges.
    Space Complexity: O(V + E)
'''
class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors

# The idea is to keep a hash_map with old-to-new node pairs while doing a DFS or a BFS on the graph.

def clone_graph(node):
    if not node:
        return None

    return dfs(node, {})


def dfs(node, old_to_new):
    if node in old_to_new:
        return old_to_new[node]

    copy = GraphNode(node.val)

    old_to_new[node] = copy

    for n in node.neighbors:
        copy.neighbors.append(dfs(n, old_to_new))

    return copy