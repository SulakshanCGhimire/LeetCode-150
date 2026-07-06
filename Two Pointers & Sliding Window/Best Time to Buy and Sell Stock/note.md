# Problem Name

121. Best Time to Buy and Sell Stock

# Difficulty

Easy

# Pattern Used

Greedy (Running Minimum)

# Approach Explanation

### Brute Force

For every day:

- Buy the stock.
- Check every future day as a possible selling day.
- Calculate the profit.
- Keep track of the maximum profit.

This guarantees the correct answer but compares every possible pair of days.

Time Complexity:

```text
O(n²)
```

which is too slow for large inputs.

---

### Optimal Approach (Used)

The best profit depends on two things:

- The lowest buying price seen so far.
- The highest profit obtainable by selling today.

Maintain two variables:

```text
min_price
max_profit
```

Traverse the array once.

For each price:

- If it is lower than the current minimum price, update `min_price`.
- Otherwise, calculate the profit if we sold today.
- Update `max_profit` if this profit is larger.

Return `max_profit` after processing all prices.

---

### Why This Works

The buying day must always come before the selling day.

Since we process prices from left to right, `min_price` always represents the cheapest stock price seen before the current day.

For every selling day, we instantly know the best buying price without searching previous elements again.

Each price is visited exactly once.

---

### Why I Used This Pattern

Indicators:

- Need to maximize a value.
- Decision depends only on previous elements.
- Only one pass through the array is necessary.
- No need to revisit earlier prices.

This is a classic Greedy problem where we continuously maintain the best buying opportunity.

---

### Could There Be A Better Version?

Current solution:

Time:

```text
O(n)
```

Space:

```text
O(1)
```

This is optimal.

Reason:

Every stock price must be inspected at least once to determine the maximum possible profit.

---

### Alternative Version

Another approach is to use Kadane's Algorithm.

Instead of working directly with prices:

- Compute the daily price differences.
- Find the maximum subarray sum.

Example:

```text
Prices:

[7,1,5,3,6,4]

Differences:

[-6,4,-2,3,-2]
```

Finding the maximum subarray gives the maximum profit.

Complexities:

Time:

```text
O(n)
```

Space:

```text
O(1)
```

Why is it not used?

Although efficient, it is less intuitive than simply tracking the minimum buying price.

The running minimum approach is easier to understand and explain during interviews.

---

### Walkthrough

Input:

```text
[7,1,5,3,6,4]
```

Initially:

```text
min_price = ∞
max_profit = 0
```

Day 1:

```text
Price = 7

min_price = 7
```

Day 2:

```text
Price = 1

min_price = 1
```

Day 3:

```text
Price = 5

Profit = 5 - 1 = 4

max_profit = 4
```

Day 4:

```text
Price = 3

Profit = 3 - 1 = 2

max_profit remains 4
```

Day 5:

```text
Price = 6

Profit = 6 - 1 = 5

max_profit = 5
```

Day 6:

```text
Price = 4

Profit = 4 - 1 = 3

max_profit remains 5
```

Final result:

```text
5
```

# Time Complexity

O(n)

Reason:

The array is traversed exactly once.

# Space Complexity

O(1)

Reason:

Only two variables are maintained regardless of input size.

# Key Learning Points

- Greedy algorithms often maintain the best value seen so far.
- A running minimum can eliminate the need for nested loops.
- Processing the array from left to right naturally satisfies the "buy before sell" condition.
- Sometimes only a few variables are enough to solve a problem efficiently.
- Always check if previous information can be reused instead of recalculating it.

# Similar Problems

- Best Time to Buy and Sell Stock II
- Maximum Difference Between Increasing Elements
- Maximum Subarray
- Maximum Product Subarray
- Longest Continuous Increasing Subsequence

# Interview Takeaway

Whenever a problem asks you to:

```text
Find the maximum gain using information from previous elements.
```

Think:

```text
Can I keep track of the best value seen so far?
```

Maintaining a running minimum or maximum is a common Greedy technique that often reduces an O(n²) solution to O(n).