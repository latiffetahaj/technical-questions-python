'''
    70. Climbing Stairs
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Constraints:
        1 <= n <= 45


    #LeetCode: https://leetcode.com/problems/climbing-stairs/description/

    Time Complexity: O(n)
    Space Complexity: O(1)
'''
# This is a dynamic programming question which we can approach it in two ways
# Bottom - Up and Top - Down approaches.

# Bottom - Up.
# Thinking about base cases:
# To arrive at step 1: only 1 way, by climbing one step.
# To arrive at step 2: 2 ways, 1 by climbing one step two times, and 1 by climbing two steps once.
# So steps = [1,2] that hold the ways to arrive at step 1, and step 2.
# Now at step 3, there are 3 ways in total, one from step 1 and 2 from step 2, therefore,
# Ways at step 3 = (Ways at step 1) + (Ways at step 2).

# To generalize:
# steps[i] = steps[i - 1] + steps[i - 2]
def climbing_stairs(n):
    # Base cases for n = 1, return 1, for n = 2, return 2.
    if n <= 2:
        return n

    previous_steps = [1,2]
    i = 3
    while i <= n:
        # Keep the previous step in a temp variable.
        temp = previous_steps[1]

        # Next step is calculated by summing up the two previous steps.
        previous_steps[1] = previous_steps[0] + previous_steps[1]

        # Update the previous step.
        previous_steps[0] = temp

        i += 1

    return previous_steps[1]