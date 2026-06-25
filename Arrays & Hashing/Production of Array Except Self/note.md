# 238. Product of Array Except Self

## Difficulty
**Medium**

## Pattern Used
**Prefix Product + Suffix Product**

---

# Approach Explanation

For every index `i`, the answer needs the product of all values except `nums[i]`.

Instead of multiplying every other element for each index, split the required product into two parts:

- Product of all elements to the **left** of `i`
- Product of all elements to the **right** of `i`

Formula:

```text
answer[i] = left_product[i] * right_product[i]
```

### Example

```text
nums = [1, 2, 3, 4]
```

For index `2`:

```text
answer[2] = 1 * 2 * 4 = 8
```

Split it into:

```text
left product  = 1 * 2 = 2
right product = 4

answer[2] = 2 * 4 = 8
```

---

# Brute Force

For every index:

1. Create a product variable.
2. Multiply every number except the current index.
3. Store the result.

### Example

For index `0`:

```text
2 * 3 * 4 = 24
```

For index `1`:

```text
1 * 3 * 4 = 12
```

### Time Complexity

```text
O(n²)
```

### Why Not Use It?

For each element, it loops through the array again.

With:

```text
n = 10⁵
```

this becomes too slow.

---

# Division Approach

A tempting solution is:

1. Find the product of all numbers.
2. For each number, divide the total product by that number.

```text
answer[i] = total_product / nums[i]
```

### Why Not Use It?

- Division is forbidden.
- It fails when the array contains zero.

### Example

```text
nums = [-1, 1, 0, -3, 3]
```

Total product becomes:

```text
0
```

Division cannot correctly produce the answer for the zero position.

---

# Optimal Approach Used

Use the output array to store prefix products first.

---

## First Pass: Prefix Products

`answer[i]` stores the product of all elements before index `i`.

```text
nums   = [1, 2, 3, 4]
answer = [1, 1, 2, 6]
```

### Explanation

```text
answer[0] = 1
answer[1] = 1
answer[2] = 1 * 2 = 2
answer[3] = 1 * 2 * 3 = 6
```

---

## Second Pass: Suffix Products

Traverse from right to left.

Maintain:

```text
suffix_product
```

which stores the product of all elements after the current index.

Multiply it into `answer[i]`.

### Initial State

```text
answer = [1, 1, 2, 6]
suffix_product = 1
```

### Iteration

```text
i = 3:
answer[3] = 6 * 1 = 6
suffix_product = 4
```

```text
i = 2:
answer[2] = 2 * 4 = 8
suffix_product = 4 * 3 = 12
```

```text
i = 1:
answer[1] = 1 * 12 = 12
suffix_product = 12 * 2 = 24
```

```text
i = 0:
answer[0] = 1 * 24 = 24
```

### Final Result

```text
[24, 12, 8, 6]
```

---

# Why This Works

At each index:

```text
answer[i] =
(product of elements before i)
*
(product of elements after i)
```

The first pass provides the left-side product.

The second pass provides the right-side product.

Multiplying both gives the product of every element except the current one.

This naturally handles zeros without requiring special cases.

---

## Example With Zero

```text
nums = [-1, 1, 0, -3, 3]
```

For the index containing `0`:

```text
(-1) * 1 * (-3) * 3 = 9
```

For every other index, the product includes zero.

Result:

```text
[0, 0, 9, 0, 0]
```

---

# Why I Used This Pattern

### Indicators for Prefix + Suffix Products

- Need results for every index.
- Each result depends on values before and after that index.
- Division is not allowed.
- Need linear time complexity.
- Need to handle zeros correctly.

This pattern is useful whenever each position needs information from **both directions**.

---

# Could There Be a Better Version?

The chosen solution is already optimal.

### Complexity

```text
Time  : O(n)
Space : O(1)
```

Every number must be processed at least once.

Therefore, time complexity cannot be better than:

```text
O(n)
```

The output array does not count as extra space.

Apart from it, we only use:

```text
prefix_product
suffix_product
```

which satisfies the follow-up requirement.

---

# Alternative Version

Use two extra arrays:

```text
prefix[i] = product of all elements before i
suffix[i] = product of all elements after i
```

Then:

```text
answer[i] = prefix[i] * suffix[i]
```

### Complexities

```text
Time  : O(n)
Space : O(n)
```

### Why Is It Worse?

It requires two additional arrays.

The optimized solution:

- Reuses the output array for prefix products.
- Uses a single variable for suffix products.

Thus extra space is reduced from:

```text
O(n) → O(1)
```

---

# Time Complexity

```text
O(n)
```

### Reason

First pass:

```text
O(n)
```

Second pass:

```text
O(n)
```

Total:

```text
O(n)
```

---

# Space Complexity

```text
O(1)
```

### Reason

The output array is not counted as extra space.

Only two variables are used:

```text
prefix_product
suffix_product
```

---

# Key Learning Points

- Prefix and suffix patterns solve "all except current index" problems efficiently.
- Division is risky when zeros exist and may be disallowed.
- Reuse the output array to reduce extra memory.
- Two directional passes can replace nested loops.
- When an answer depends on both sides of an index, think **Prefix + Suffix**.

---

# Similar Problems

- Trapping Rain Water
- Range Sum Query
- Maximum Product Subarray
- Pivot Index
- Find Pivot Index
- Maximum Sum Circular Subarray

---

# Interview Takeaway

When a problem asks:

> For each index, calculate something using every element except itself.

Think:

```text
Can I split the result into:
left contribution × right contribution?
```

For multiplication problems, the standard optimal pattern is:

## Prefix Product + Suffix Product

This gives:

```text
Time  : O(n)
Space : O(1)
```

while correctly handling zeros and avoiding division.