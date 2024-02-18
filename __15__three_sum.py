'''
    15. 3Sum
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Constraints:
        3 <= nums.length <= 3000
        -10^5 <= nums[i] <= 10^5

    #LeetCode: https://leetcode.com/problems/3sum/description/

    Time Complexity: O(n^2)

    Space Complexity: O(1) or in some cases if sorting uses extra space, then O(n)


'''

def three_sum(nums):
    result = []
    nums.sort()

    for i, value in enumerate(nums):
        #to avoid duplicates, only consider different numbers in the first position
        if i > 0 and value == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            three_sum = value + nums[l] + nums[r]

            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                result.append([value,nums[l], nums[r]])

                #fixing the first number, there may be more than one solution to the rest of the array
                #that can sum up to 0, therefore to avoid duplicates, keep moving the left pointer until
                #a different number is considered for the second position in the triplet.
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return result