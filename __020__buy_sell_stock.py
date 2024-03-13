'''
    121. Best Time to Buy and Sell Stock
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Constraints:
        1 <= prices.length <= 10^5
        0 <= prices[i] <= 10^4

    #LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

    Time Complexity: O(n)

    Space Complexity: O(1)
'''

def max_profit(prices):

    max_profit = 0
    buy = 0
    sell = 1

    while sell < len(prices):
        if prices[sell] > prices[buy]:
            current_profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, current_profit)
        else:
            #when price of selling is lower than price of buying, that means a better price to buy was found so
            buy = sell

        sell += 1

    return max_profit
