# Problem Name

54. Spiral Matrix

# Difficulty

Medium

# Pattern Used

Matrix Traversal (Boundary Simulation)

# Approach Explanation

### Brute Force

Simulate movement one cell at a time.

- Move right until blocked.
- Turn down.
- Turn left.
- Turn up.
- Keep repeating while marking visited cells.

Why not use this?

- Requires a separate visited matrix.
- More complex direction handling.
- Extra space is needed.

---

### Better Approach

Maintain four boundaries:

```text
top
bottom
left
right
```

Traverse the matrix layer by layer.

After finishing one side, move the corresponding boundary inward.

Repeat until all elements are visited.

---

### Optimal Approach (Used)

Maintain four pointers:

```text
top = 0
bottom = rows - 1
left = 0
right = cols - 1
```

Process the matrix in four directions:

1. Left → Right
2. Top → Bottom
3. Right → Left
4. Bottom → Top

After each traversal, shrink the corresponding boundary.

Example:

```text
1 2 3
4 5 6
7 8 9
```

Left → Right

```text
1 2 3
```

Move:

```text
top++
```

---

Top → Bottom

```text
6
9
```

Move:

```text
right--
```

---

Right → Left

```text
8 7
```

Move:

```text
bottom--
```

---

Bottom → Top

```text
4
```

Move:

```text
left++
```

Now only:

```text
5
```

remains.

Final order:

```text
[1,2,3,6,9,8,7,4,5]
```

---

### Why This Works

Each iteration completes one outer "layer" of the matrix.

After visiting a side, that side is no longer needed.

Moving the boundaries inward ensures:

- No element is visited twice.
- Every element is visited exactly once.

The boundary checks:

```text
if top <= bottom
```

and

```text
if left <= right
```

prevent duplicate traversals when only one row or one column remains.

---

### Why I Used This Pattern

Indicators:

- Need to traverse a matrix in a specific order.
- Traversal happens layer by layer.
- No modification of the matrix is required.
- Boundaries naturally define the remaining unvisited region.

Boundary simulation is the cleanest solution.

---

### Could There Be A Better Version?

Current solution:

Time:

```text
O(m × n)
```

Space:

```text
O(1)
```

(extra space excluding the output list)

This is optimal.

Reason:

Every element must be visited exactly once.

---

### Alternative Version

Use:

- Direction arrays
- Visited matrix

Example:

```text
Right
↓

Down
↓

Left
↓

Up
```

Whenever movement becomes invalid:

- Turn clockwise.

Complexities:

Time:

```text
O(m × n)
```

Space:

```text
O(m × n)
```

Why is it worse?

- Requires a visited matrix.
- More complicated implementation.
- Boundary traversal is simpler.

---

### Walkthrough

Input:

```text
1 2 3
4 5 6
7 8 9
```

Initial boundaries:

```text
top = 0
bottom = 2
left = 0
right = 2
```

Traverse:

```text
1 2 3
```

Update:

```text
top = 1
```

Traverse:

```text
6 9
```

Update:

```text
right = 1
```

Traverse:

```text
8 7
```

Update:

```text
bottom = 1
```

Traverse:

```text
4
```

Update:

```text
left = 1
```

Remaining:

```text
5
```

Final result:

```text
[1,2,3,6,9,8,7,4,5]
```

# Time Complexity

O(m × n)

Reason:

Every matrix element is visited exactly once.

# Space Complexity

O(1)

Reason:

Only four boundary variables are used.

The output list is not counted as extra space.

# Key Learning Points

- Boundary pointers simplify matrix traversal.
- Shrink the search area after each completed side.
- Always check boundaries before traversing the bottom row or left column.
- Spiral traversal processes the matrix layer by layer.
- Avoid a visited matrix when boundary simulation is sufficient.

# Similar Problems

- Spiral Matrix II
- Rotate Image
- Set Matrix Zeroes
- Game of Life
- Diagonal Traverse

# Interview Takeaway

Whenever a problem asks:

```text
Traverse a matrix layer by layer.
```

Think:

```text
Can I maintain four boundaries?
```

The four-boundary technique is the standard solution for spiral traversal and many other matrix simulation problems.