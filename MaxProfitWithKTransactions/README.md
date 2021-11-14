## MAX PROFIT WITH K TRANSACTIONS

In share trading, a buyer buys shares and sells on a future date. Given the stock price of n days,
the trader is allowed to make at most k transactions, where a new transaction can only start after the previous
transaction is complete, find out the maximum profit that a share trader could have made.

### EXAMPLES

#### Example 1
Price = [10, 22, 5, 75, 65, 80] <br />
K = 2 <br />
Output: 87. Trader earns 87 as sum of 12 and 75 Buy at price 10, sell at 22, buy at 5 and sell at 80

#### Example 2
Price = [12, 14, 17, 10, 14, 13, 12, 15] <br />
K = 3 <br />
Output: 12. Trader earns 12 as the sum of 5, 4 and 3.<br />
Buy at price 12, sell at 17, buy at 10 and sell at 14 and buy at 12 and sell at 15 <br />

#### Example 3
Price = [90, 80, 70, 60, 50] <br />
K = 1 <br />
Output: 0 Not possible to earn <br />


