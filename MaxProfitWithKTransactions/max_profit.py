# In share trading, a buyer buys shares and sells on a future date. Given the stock price of n days,
# the trader is allowed to make at most k transactions, where a new transaction can only start after the previous
# transaction is complete, find out the maximum profit that a share trader could have made.

# EXAMPLES

# Input:
# Price = [10, 22, 5, 75, 65, 80]
# K = 2
# Output: 87. Trader earns 87 as sum of 12 and 75 Buy at price 10, sell at 22, buy at 5 and sell at 80
#
# Input:
# Price = [12, 14, 17, 10, 14, 13, 12, 15]
# K = 3
# Output: 12. Trader earns 12 as the sum of 5, 4 and 3.
# Buy at price 12, sell at 17, buy at 10 and sell at 14 and buy at 12 and sell at 15
#
#
# Input:
# Price = [90, 80, 70, 60, 50]
# K = 1
# Output: 0 Not possible to earn

#
#   Method used to calculate profits O(nk) time | O(nk) space
#
def maxProfitWithKTransactions(prices, k):
    _max_profit = 0

    if not len(prices):
        return 0

    profits = [[0 for d in prices] for t in range(k + 1)]
    print(profits)

    for t in range(1, k + 1):
        _max_profit = float("-inf")
        for d in range(1, len(prices)):
            _max_profit = max(_max_profit, profits[t - 1][d - 1] - prices[d - 1])
            profits[t][d] = max(profits[t][d-1], _max_profit + prices[d])

    return profits[-1][-1]


#
#   Method used to calculate profits O(nk) time | O(n) space
#   The only difference with previous method is that we don't use the whole array but just the last 2 rows
def maxProfitWithKTransactionsSimpler(prices, k):
    _max_profit = 0

    if not len(prices):
        return 0

    evenProfits = [0 for d in prices]
    oddProfits = [0 for d in prices]

    for t in range(1, k + 1):
        _max_profit = float("-inf")
        if t % 2 == 1:
            currentProfits = oddProfits
            previousProfits = evenProfits
        else:
            currentProfits = evenProfits
            previousProfits = oddProfits

        for d in range(1, len(prices)):
            _max_profit = max(_max_profit, previousProfits[d - 1] - prices[d - 1])
            currentProfits[d] = max(currentProfits[d - 1], _max_profit + prices[d])

    return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]


#
# Main script
#
if __name__ == '__main__':
    _prices = [90, 80, 70, 60, 50]
    _transactions = 1
    max_profit = maxProfitWithKTransactionsSimpler(_prices, _transactions)
    print(max_profit)
