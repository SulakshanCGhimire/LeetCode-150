# Problem Name

189. Rotate Array

# Difficulty

Medium

# Pattern Used

Array Reversal (In-place)

# Approach Explanation

### Brute Force

Rotate the array one step at a time.

Example:

```text
nums = [1,2,3,4,5,6,7]
k = 3
```

Rotation 1:

```text
[7,1,2,3,4,5,6]
```

Rotation 2:

```text
[6,7,1,2,3,4,5]
```

Rotation 3:

```text
[5,6,7,1,2,3,4]
```

Why not use this?

Time Complexity:

```text
O(n × k)
```

If `k` is very large, this becomes inefficient.

---

### Better Approach

Create another array.

For every element:

```text
new[(i + k) % n] = nums[i]
```

Example:

```text
nums = [1,2,3,4,5,6,7]
k = 3
```

Result:

```text
[5,6,7,1,2,3,4]
```

Time:

```text
O(n)
```

Space:

```text
O(n)
```

Why not use it?

The problem requires modifying the array **in-place**.

---

### Optimal Approach (Used)

Use the **Reversal Algorithm**.

Steps:

1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining elements.

Example:

```text
nums = [1,2,3,4,5,6,7]
k = 3
```

Step 1:

Reverse entire array.

```text
[7,6,5,4,3,2,1]
```

Step 2:

Reverse first `k` elements.

```text
[5,6,7,4,3,2,1]
```

Step 3:

Reverse remaining elements.

```text
[5,6,7,1,2,3,4]
```

Final answer:

```text
[5,6,7,1,2,3,4]
```

Before rotating:

Always compute:

```text
k = k % n
```

This handles cases where `k` is greater than the array length.

Example:

```text
n = 7
k = 10

k = 10 % 7 = 3
```

Rotating 10 times is equivalent to rotating 3 times.

---

### Why This Works

Reversing the entire array moves the last `k` elements to the front, but in reverse order.

Reversing the first part restores the correct order of those moved elements.

Reversing the remaining part restores the order of the remaining elements.

Together, the three reversals produce the desired rotation without extra memory.

---

### Why I Used This Pattern

Indicators:

- Problem must be solved in-place.
- Constant extra space required.
- Entire array needs rearrangement.
- Reversal can transform the array efficiently.

The reversal technique is the standard optimal solution for in-place array rotation.

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

Every element must move at least once.

The follow-up requires modifying the array in-place, which this solution satisfies.

---

### Alternative Version

Use an extra array.

```text
new[(i + k) % n] = nums[i]
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

Why is it worse?

- Requires additional memory.
- Does not satisfy the in-place requirement.

---

### Walkthrough

Input:

```text
nums = [1,2,3,4,5,6,7]
k = 3
```

Reverse all:

```text
[7,6,5,4,3,2,1]
```

Reverse first three:

```text
[5,6,7,4,3,2,1]
```

Reverse remaining:

```text
[5,6,7,1,2,3,4]
```

Return modified array.

# Time Complexity

O(n)

Reason:

- Reverse entire array → O(n)
- Reverse first k elements → O(k)
- Reverse remaining elements → O(n-k)

Overall:

```text
O(n)
```

# Space Complexity

O(1)

Reason:

Only a few temporary variables are used during swapping.

No additional array is created.

# Key Learning Points

- Reverse operations can replace extra memory.
- Always reduce `k` using modulo before rotating.
- In-place array manipulation is a common interview topic.
- Three reversals achieve rotation efficiently.
- Think about transforming the array instead of shifting elements repeatedly.

# Similar Problems

- Rotate Image
- Set Matrix Zeroes
- Next Permutation
- Move Zeroes
- Wiggle Sort

# Interview Takeaway

Whenever a problem asks:

```text
Rotate an array in-place.
```

Think:

```text
Can reversing parts of the array achieve the required order?
```

The **three-reversal algorithm** is the standard optimal solution:

1. Reverse the whole array.
2. Reverse the first `k` elements.
3. Reverse the remaining elements.

This achieves **O(n)** time and **O(1)** extra space.