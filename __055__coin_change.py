'''
    322. Coin Change
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.

    Constraints:
        1 <= coins.length <= 12
        1 <= coins[i] <= 2^31 - 1
        0 <= amount <= 10^4


    #LeetCode: https://leetcode.com/problems/coin-change/description/

    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
'''

# The idea is to allocate an extra array that will keep the least amount of coins at each step from 0 up to the amount
# i-th position depends on the previous positions in this way:
# It calculates the minimum amount of coins to arrive at this position by looking at the [i - coin] position and adding one for this extra coin that we want to calculate.


def coin_change(coins, amount):

    # The default value is choosen to be amount + 1 because this is the upper bound on the number of coins that we can use to arrive at the amount.
    least_coins_at = [amount + 1] * (amount + 1)

    # To give change of 0, we can use zero coins.
    least_coins_at[0] = 0

    for i in range(1,amount + 1):
        for c in coins:
            if i - c >= 0:
                least_coins_at[i] = min(least_coins_at[i], 1 + least_coins_at[i - c])


    # If this amount still holds the default value, that means we can't make up the amount using these coins so return -1.
    if least_coins_at[amount] == (amount + 1):
        return - 1
    else:
        return least_coins_at[amount]
