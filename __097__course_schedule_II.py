'''
    210. Course Schedule II
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
    You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates that you must take course b_i first if you want to take course a_i.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return the ordering of courses you should take to finish all courses.
    If there are many valid answers, return any of them.
    If it is impossible to finish all courses, return an empty array.

    Constraints:
        1 <= numCourses <= 2000
        0 <= prerequisites.length <= numCourses * (numCourses - 1)
        prerequisites[i].length == 2
        0 <= ai, bi < numCourses
        ai != bi
        All the pairs [ai, bi] are distinct.


    #LeetCode: https://leetcode.com/problems/course-schedule-ii/

    Time Complexity: O(V + E) V - number of courses, E - edges in the prerequisites array.
    Space Complexity: O(V + E)
'''
from collections import defaultdict

def find_order(num_courses, prerequisites):
    visited = set()
    path = set()
    top_sort = []

    adjList = defaultdict(list)

    for src, dst in prerequisites:
        adjList[src].append(dst)


    for i in range(num_courses):
        if not dfs(i, adjList, path, visited, top_sort):
            return []

    return top_sort

# DFS checks for cycles and also builds the topological sort in the post-order traversal.
def dfs(node, adjList, path, visited, top_sort):
    if node in path:
        return False

    if node in visited:
        return True

    visited.add(node)
    path.add(node)

    for n in adjList[node]:
        if not dfs(n, adjList, path, visited, top_sort):
            return False

    path.remove(node)
    top_sort.append(node)
    return True