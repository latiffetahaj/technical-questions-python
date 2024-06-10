'''
    207. Course Schedule
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.

    Constraints:
        1 <= numCourses <= 2000
        0 <= prerequisites.length <= 5000
        prerequisites[i].length == 2
        0 <= ai, bi < numCourses
        All the pairs prerequisites[i] are unique.

    #LeetCode: https://leetcode.com/problems/course-schedule/

    Time Complexity: O(V + E)

    Space Complexity: O(V + E)
'''
from collections import defaultdict

# The solution follows the topological sort algorithm.
# If there's any cycle detected, that means the courses cannot be completed so return False, otherwise return True.
# To check for cycles, we use DFS algorithm.

def can_finish(num_courses, prerequisites):
    # Build an adjacency list
    adj = defaultdict(list)
    visit = set()
    path = set()

    for src, dst in prerequisites:
        adj[src].append(dst)


    for i in range(num_courses):
        if not dfs(i, adj, visit, path):
            return False

    return True


def dfs(node, adj, visit, path):
    if node in path:
        return False

    if node in visit:
        return True

    visit.add(node)
    path.add(node)

    for n in adj[node]:
        if not dfs(n, adj, visit, path):
            return False

    path.remove(node)
    return True

