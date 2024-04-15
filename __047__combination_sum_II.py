'''
    40. Combination Sum II
    Given a collection of candidate numbers (candidates) and a target number (target),
    find all unique combinations in candidates where the candidate numbers sum to target.

    Each number in candidates may only be used once in the combination.
    Note: The solution set must not contain duplicate combinations.

    Constraints:
        1 <= candidates.length <= 100
        1 <= candidates[i] <= 50
        1 <= target <= 30

    #LeetCode: https://leetcode.com/problems/combination-sum-ii/description/

    Time Complexity: O(n!) to generate all the combinations

    Space Complexity: The smallest value that a candidate can have is 1.
                    To sum up to the target value: 1 + 1 + 1 + 1... = target
                    Therefore, on the recursion stack, at most there will be O(target) calls at the same time so space on stack O(target)

                    For the result: At most there will be n! / (k! * (n - k)!) combinations, roughly O(n!) for the result
'''
# Algorithm is as follows:
# Sort the input.
# Use a list to keep the current combination.
# If sum of current combination == target, append to the result list.
# If sum of current combination > target, pop the last element and consider other candidates.
# For this current position, only consider candidates that are different than the last, to prevent duplicates.

def combination_sum_II(candidates, target):
    # Sorting the input makes it easier to skip duplicates.
    candidates.sort()

    result = []
    generate_combinations_II(candidates, result, [], 0, target, 0)

    return result



def generate_combinations_II(candidates, result, current, total, target, starting_index):
    if total == target:
        result.append(current.copy())
        return

    if total > target:
        return

    if starting_index >= len(candidates):
        return

    i = starting_index

    while i < len(candidates):
        current.append(candidates[i])

        # Recursive call.
        generate_combinations_II(candidates, result, current, total + candidates[i], target, i + 1)

        current.pop()

        # If the total + candidates[i] is greater than target, break the loop.
        # Because the input is sorted then all the other candidates are larger than this one, so discard all of them.
        if total + candidates[i] > target:
            break

        # Skip duplicates.
        while (i + 1) < len(candidates) and candidates[i + 1] == candidates[i]:
            i += 1

        # Iterate over the next candidate.
        i += 1


    return