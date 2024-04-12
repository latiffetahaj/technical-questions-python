'''
    39. Combination Sum
    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
    You may return the combinations in any order.
    The same number may be chosen from candidates an unlimited number of times.
    Two combinations are unique if the frequency of at least one of the chosen numbers is different.

    The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

    Constraints:
        1 <= candidates.length <= 30
        2 <= candidates[i] <= 40
        All elements of candidates are distinct.
        1 <= target <= 40


    #LeetCode: https://leetcode.com/problems/combination-sum/description/

    Time Complexity: These are combinations with replacement so it is a factorial time complexity
                    O(n!)

    Space Complexity: Smallest input is 1, so the max depth of the recursive calls can be at most target
                        1 + 1 + 1 + 1 .... = target
                    O(target) on the stack due to recursive calls

'''

def combination_sum(candidates, target):
    result = []
    current = []

    input_length = len(candidates)

    generate_comb(candidates, result, current, 0, target, 0, input_length)

    return result



def generate_comb(candidates,result,current,total,target, starting_index, input_length):
    # If a combination sums up to target, append it to the result list.
    if total == target:
        result.append(current.copy())
        return

    # Backtrack and remove the last value, to check for different combinations.
    if total > target:
        return

    for i in range(starting_index, input_length):
        current.append(candidates[i])

        # Since it's a combination with replacement, use this candidate as well, so starting_index = i
        generate_comb(candidates,result,current, total + candidates[i], target, i, input_length)

        current.pop()

    return
