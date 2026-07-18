# Problem Name

11. Container With Most Water

# Difficulty

Medium

# Pattern Used

Two Pointers (Greedy)

# Approach Explanation

### Brute Force

Consider every possible pair of lines.

For every pair:

- Calculate the width.
- Find the shorter line.
- Compute the area.
- Keep track of the maximum area.

Formula:

```text
Area = (right - left) × min(height[left], height[right])
```

Time Complexity:

```text
O(n²)
```

This is too slow because every pair of lines is examined.

---

### Optimal Approach (Used)

Use two pointers.

Initialize:

```text
left = 0

right = n - 1
```

These pointers represent the widest possible container.

For every iteration:

- Calculate the current area.
- Update the maximum area.
- Move the pointer with the **smaller height**.

Reason:

The height of the container is limited by the shorter line.

Moving the taller line inward only decreases the width while the height remains limited by the shorter line, so it cannot produce a better result.

Continue until both pointers meet.

---

### Why This Works

The area depends on two values:

```text
Width × Minimum Height
```

As the pointers move inward,

the width always decreases.

Therefore, the only chance to obtain a larger area is to increase the limiting height.

The limiting height is always the shorter line.

By moving the shorter pointer, we may find a taller line that compensates for the reduced width.

Moving the taller pointer cannot increase the limiting height.

Thus, we safely discard impossible candidates without missing the optimal answer.

---

### Why I Used This Pattern

Indicators:

- Need to maximize a value using two ends of an array.
- Width depends on the distance between two indices.
- Decision depends on comparing both ends.
- A greedy observation allows one pointer to move safely.

These are classic characteristics of the **Two Pointers** pattern.

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

Every line is visited at most once.

No algorithm can do better because every height may influence the answer.

---

### Alternative Version

The only straightforward alternative is the brute-force approach.

Steps:

- Fix one line.
- Pair it with every line to its right.
- Compute every possible area.

Complexities:

Time:

```text
O(n²)
```

Space:

```text
O(1)
```

Why is it not used?

It repeatedly computes areas for pairs that can be eliminated using the greedy observation.

The Two Pointer approach avoids unnecessary comparisons.

---

### Walkthrough

Input:

```text
height = [1,8,6,2,5,4,8,3,7]
```

Initially:

```text
left = 0

right = 8
```

Area:

```text
Width = 8

Height = min(1,7) = 1

Area = 8
```

Move:

```text
left
```

because

```text
1 < 7
```

Now:

```text
left = 1

right = 8
```

Area:

```text
Width = 7

Height = min(8,7) = 7

Area = 49
```

Maximum:

```text
49
```

Continue moving the smaller pointer.

No later container produces a larger area.

Final answer:

```text
49
```

---

# Time Complexity

```text
O(n)
```

Reason:

Each pointer moves toward the center at most once.

---

# Space Complexity

```text
O(1)
```

Reason:

Only a few variables are maintained.

---

# Key Learning Points

- The container's height is determined by the shorter line.
- Always move the pointer pointing to the shorter line.
- The width decreases every iteration, so increasing the limiting height is the only way to improve the area.
- Two Pointers can reduce a quadratic solution to linear time.
- Greedy observations often make pointer movement safe.

---

# Similar Problems

- Trapping Rain Water
- Two Sum II - Input Array Is Sorted
- 3Sum
- Boats to Save People
- Squares of a Sorted Array

---

# Interview Takeaway

Whenever a problem asks:

```text
Find the best pair of elements from both ends of an array.
```

Think:

```text
Two Pointers
```

If moving one pointer can safely eliminate impossible candidates using a greedy observation, you can often reduce an **O(n²)** solution to **O(n)**. In this problem, moving the shorter line is the key insight because only a taller line can potentially produce a larger area despite the decreasing width.