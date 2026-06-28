# Problem Name

73. Set Matrix Zeroes

# Difficulty

Medium

# Pattern Used

Matrix Traversal + In-place Marking

# Approach Explanation

### Brute Force

Whenever a zero is found:

- Immediately set its entire row to zero.
- Immediately set its entire column to zero.

Why not use this?

Example:

```text
1 1 1
1 0 1
1 1 1
```

If we instantly modify the matrix, the newly created zeros will also be treated as original zeros.

This causes incorrect results because we lose information about which zeros were originally present.

---

### Better Approach

Store all rows and columns that contain a zero.

Example:

```text
rows = {1}
cols = {1}
```

After scanning the matrix:

- Zero every row in `rows`.
- Zero every column in `cols`.

Time:

```text
O(m × n)
```

Space:

```text
O(m + n)
```

Why not use it?

Although efficient, the follow-up asks for **constant extra space**.

---

### Optimal Approach (Used)

Use the **first row** and **first column** as markers.

Whenever a zero is found:

```text
matrix[r][0] = 0
matrix[0][c] = 0
```

These cells indicate that the entire row or column should become zero later.

Since the first row and first column are now being used as markers, we must first remember whether they originally contained a zero.

```text
first_row_zero
first_col_zero
```

Finally:

1. Mark rows and columns.
2. Zero marked rows.
3. Zero marked columns.
4. Zero the first row if needed.
5. Zero the first column if needed.

---

### Why This Works

The first row stores which columns should become zero.

The first column stores which rows should become zero.

Example:

```text
1 1 1
1 0 1
1 1 1
```

After marking:

```text
1 0 1
0 0 1
1 1 1
```

The markers indicate:

- Row 1 becomes zero.
- Column 1 becomes zero.

After applying them:

```text
1 0 1
0 0 0
1 0 1
```

The original information is preserved without allocating extra arrays.

---

### Why I Used This Pattern

Indicators:

- Problem must be solved in-place.
- Extra space should be constant.
- Existing matrix can be reused for bookkeeping.
- Follow-up specifically asks for O(1) extra space.

Using the first row and first column as markers eliminates the need for additional storage.

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

This is optimal.

Reason:

Every cell must be inspected at least once.

The follow-up explicitly asks for constant extra space, which this solution satisfies.

---

### Alternative Version

Use two Hash Sets.

Example:

```text
rows = set()
cols = set()
```

First pass:

Store every row and column containing a zero.

Second pass:

Zero cells whose row or column appears in the sets.

Complexities:

Time:

```text
O(m × n)
```

Space:

```text
O(m + n)
```

Why is it worse?

- Requires additional memory.
- Does not satisfy the follow-up.

---

### Walkthrough

Input:

```text
1 1 1
1 0 1
1 1 1
```

Step 1

Check first row and first column.

Neither contains a zero.

---

Step 2

Find zero at:

```text
(1,1)
```

Mark:

```text
matrix[1][0] = 0
matrix[0][1] = 0
```

Matrix becomes:

```text
1 0 1
0 0 1
1 1 1
```

---

Step 3

Zero marked rows.

```text
1 0 1
0 0 0
1 1 1
```

---

Step 4

Zero marked columns.

```text
1 0 1
0 0 0
1 0 1
```

Return modified matrix.

# Time Complexity

O(m × n)

Reason:

- One pass to detect markers.
- One pass to update rows.
- One pass to update columns.

Overall:

```text
O(m × n)
```

# Space Complexity

O(1)

Reason:

Only two boolean variables are used.

The matrix itself stores all row and column markers.

# Key Learning Points

- In-place problems often reuse the input for bookkeeping.
- Avoid modifying values immediately if future decisions depend on the original matrix.
- The first row and first column can act as marker arrays.
- Always preserve the original state of marker rows or columns before reusing them.
- Follow-up constraints often hint at the intended optimization.

# Similar Problems

- Game of Life
- Rotate Image
- Spiral Matrix
- Product of Array Except Self
- Valid Sudoku

# Interview Takeaway

Whenever a problem says:

```text
Modify the matrix in-place.
```

Think:

```text
Can part of the matrix itself be reused as extra storage?
```

This technique is a common optimization for matrix problems and is frequently tested in interviews.