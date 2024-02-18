'''
    11. Container With Most Water
    You are given an integer array height of length n.
    There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    Constraints:
        n == height.length
        2 <= n <= 10^5
        0 <= height[i] <= 10^4

    #LeetCode: https://leetcode.com/problems/container-with-most-water/description/

    Time Complexity: O(n)

    Space Complexity: O(1)
'''

def most_water_container(height):
    max_area = 0

    l = 0
    r = len(height) - 1

    while l < r:
        left_height = height[l]
        right_height = height[r]

        # area = (distance between two pointers) x (which height is smaller)
        if left_height > right_height:
            current_area = (r - l) * right_height
            r -= 1
        else:
            current_area = (r - l) * left_height
            l += 1

        if current_area > max_area:
            max_area = current_area

    return max_area
