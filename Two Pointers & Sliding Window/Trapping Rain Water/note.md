# Problem Name

42. Trapping Rain Water

# Difficulty

Hard

# Pattern Used

Two Pointers + Prefix Maximum Tracking

# Approach Explanation

### Brute Force

For every index:

- Find the tallest bar to its left.
- Find the tallest bar to its right.
- The water trapped at that index is:

```text
min(left_max, right_max) - height[i]
```

If the result is positive, add it to the answer.

This approach is correct but repeatedly searches for maximum heights.

Time Complexity:

```text
O(n²)
```

which is inefficient.

---

### Prefix/Suffix Maximum Arrays

A better approach is to precompute:

```text
left_max[i]
```

which stores the tallest bar to the left of index `i`.

And:

```text
right_max[i]
```

which stores the tallest bar to the right of index `i`.

Then:

```text
water_at_i = min(left_max[i], right_max[i]) - height[i]
```

This gives:

Time:

```text
O(n)
```

Space:

```text
O(n)
```

However, the extra arrays are unnecessary.

---

### Optimal Approach (Used)

Use two pointers:

```text
left
right
```

Also maintain:

```text
left_max
right_max
```

These store the highest bars seen from each side.

The amount of water above a bar depends on:

```text
min(left_max, right_max)
```

At each step:

- If `height[left] <= height[right]`, process the left side.
- Otherwise, process the right side.

When processing the left side:

```text
if height[left] >= left_max:
    update left_max
else:
    add left_max - height[left]
```

Similarly for the right side.

---

### Why This Works

Suppose:

```text
height[left] <= height[right]
```

The right side already has a boundary at least as tall as the current left bar.

Therefore, the amount of water at the left position is determined by:

```text
left_max
```

The right side cannot be the limiting factor at this moment.

So we can safely calculate the trapped water on the left and move the left pointer inward.

The same logic applies symmetrically to the right side.

---

### Why I Used This Pattern

Indicators:

- Water at an index depends on the maximum height on both sides.
- Need to avoid repeatedly scanning left and right.
- The array can be processed from both ends.
- Extra prefix/suffix arrays can be replaced with a few variables.

This is a classic **Two Pointer + Running Maximum** problem.

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

This is optimal in both time and extra space.

Every bar is processed once.

---

### Alternative Version

Use prefix and suffix maximum arrays.

Example:

```text
left_max[i]
right_max[i]
```

Then calculate:

```text
min(left_max[i], right_max[i]) - height[i]
```

Complexities:

Time:

```text
O(n)
```

Space:

```text
O(n)
```

Why is it not used?

It is easier to visualize and explain, but the two-pointer approach achieves the same time complexity using constant extra space.

---

### Another Alternative

Use a Monotonic Stack.

The stack stores indices of bars that have not yet found a taller right boundary.

When a taller bar appears:

- Pop a lower bar.
- Calculate the bounded water.
- Use the current bar as the right boundary.

Complexities:

Time:

```text
O(n)
```

Space:

```text
O(n)
```

Why is it not used?

The stack solution is powerful but more complex.

The two-pointer approach is simpler when only the total amount of water is required.

---

### Walkthrough

Input:

```text
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

Initially:

```text
left = 0

right = 11

left_max = 0

right_max = 0

water = 0
```

The pointers move inward.

Whenever a bar is lower than the maximum boundary on its side, water is added.

For example:

```text
height = 0
left_max = 1
```

Water trapped:

```text
1 - 0 = 1
```

Another lower section:

```text
height = 0
left_max = 2
```

Water is added based on the available boundary.

Across all positions, the total becomes:

```text
6
```

Final result:

```text
6
```

---

# Time Complexity

```text
O(n)
```

Reason:

Each pointer moves inward at most once.

Every bar is processed a constant number of times.

---

# Space Complexity

```text
O(1)
```

Reason:

Only two pointers, two running maximums, and the answer variable are used.

---

# Key Learning Points

- Water trapped at an index depends on the shorter boundary.
- Prefix and suffix maximum arrays can often be optimized using two pointers.
- Running maximums allow us to avoid repeated scanning.
- The side with the smaller current boundary can be safely processed.
- Two Pointer solutions can reduce both time and space complexity.

---

# Similar Problems

- Container With Most Water
- Largest Rectangle in Histogram
- Daily Temperatures
- Sliding Window Maximum
- Monotonic Stack Problems

---

# Interview Takeaway

Whenever a problem asks:

```text
How much can be trapped between elements?
```

Think:

```text
What is the maximum boundary on the left and right?
```

For Trapping Rain Water:

```text
Water at i =
min(max height on left, max height on right) - height[i]
```

The key optimization is realizing that the left and right maximums can be tracked with two pointers instead of storing entire prefix and suffix arrays.

This gives:

```text
O(n) time
O(1) extra space
```