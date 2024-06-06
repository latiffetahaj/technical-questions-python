'''
    1046. Last Stone Weight
    You are given an array of integers stones where stones[i] is the weight of the ith stone.

    We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
    At the end of the game, there is at most one stone left.

    Return the weight of the last remaining stone. If there are no stones left, return 0.

    Constraints:
        1 <= stones.length <= 30
        1 <= stones[i] <= 1000


    #LeetCode: https://leetcode.com/problems/last-stone-weight/

    Time Complexity: O(n logn), O(n) to heapify + O(nlogn) to pop n times, overall O(nlogn)
    Space Complexity: O(1)
'''
import heapq

# We use a max-heap data structure. In python to simulate a max heap, we multiply all the values by -1.
def last_stone_weight(stones):
    # Convert to negative.
    stones = [s * (-1) for s in stones]

    heapq.heapify(stones)

    while len(stones) >= 2:
        y = -1 * heapq.heappop(stones)
        x = -1 * heapq.heappop(stones)

        if x != y:
            y = y - x
            heapq.heappush(stones, -1 * y)

    return -1 * stones[0] if len(stones) > 0 else 0