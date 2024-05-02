'''
    746. Min Cost Climbing Stairs
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
    You can either start from the step with index 0, or the step with index 1.
    Return the minimum cost to reach the top of the floor.

    Constraints:
        2 <= cost.length <= 1000
        0 <= cost[i] <= 999


    #LeetCode: https://leetcode.com/problems/min-cost-climbing-stairs/

    Time Complexity: O(n)
    Space Complexity: O(1)
'''

# A Bottom - Up dynamic programming approach
# Since you can take 1 step or 2 steps at a time, current step cost depends on the relation:
# cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
# The top is located at the last_index + 1, or at the index = len(cost)
# Therefore to make room for the top, we append a zero at the end.
# Since we can start from index 0 or 1, we traverse the cost array from index 2 all the way to the end.

def min_cost_climbing(cost):
    cost.append(0)

    for i in range(2, len(cost)):
        cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])

    # Return the value at the last index.
    return cost[-1]

