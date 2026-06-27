# Problem Name

36. Valid Sudoku

# Difficulty

Medium

# Pattern Used

Hash Set

# Approach Explanation

### Brute Force

For every filled cell:

- Check the entire row.
- Check the entire column.
- Check the entire 3×3 box.

Repeat this for every cell.

Why not use this?

- The same rows, columns, and boxes are checked repeatedly.
- Performs unnecessary duplicate work.
- Time Complexity is approximately O(n³) for a general Sudoku board.

---

### Better Approach

Maintain separate data structures for:

- Each row
- Each column
- Each 3×3 box

As we traverse the board:

1. Ignore empty cells (`.`).
2. Check whether the current number already exists in:
   - its row
   - its column
   - its box
3. If it exists anywhere, return `False`.
4. Otherwise, store it.

---

### Optimal Approach (Used)

Use three arrays of Hash Sets.

```text
rows[9]
cols[9]
boxes[9]
```

Each set stores the numbers already seen.

For every cell:

```text
value = board[r][c]
```

If the cell is empty:

```text
continue
```

Find which 3×3 box the cell belongs to.

```text
box = (r // 3) * 3 + (c // 3)
```

Then check:

```text
value in rows[r]

value in cols[c]

value in boxes[box]
```

If any are true:

```text
return False
```

Otherwise add the value into all three sets.

---

### Why This Works

A Sudoku board is valid only if:

- Every row contains unique numbers.
- Every column contains unique numbers.
- Every 3×3 box contains unique numbers.

The Hash Sets record every number that has already appeared.

Whenever a duplicate is found, the board becomes invalid immediately.

---

### Why I Used This Pattern

Indicators:

- Need to detect duplicates.
- Fast lookup is required.
- Multiple independent groups must be validated.
- Order of elements does not matter.

Hash Sets provide:

- O(1) insertion
- O(1) lookup

making them ideal.

---

### Could There Be A Better Version?

Current solution:

Time:

O(1)

Space:

O(1)

Although we visit every cell, Sudoku always contains only:

```text
9 × 9 = 81 cells
```

Therefore the running time is constant.

---

### Alternative Version

Use one Hash Set instead.

Store unique identifiers.

Example:

```text
("row", r, value)

("col", c, value)

("box", box, value)
```

If any identifier already exists:

```text
return False
```

Complexities:

Time:

O(1)

Space:

O(1)

Why is it worse?

- Less intuitive.
- Harder to understand.
- Three separate Hash Sets are cleaner.

---

### Walkthrough

Example:

```text
5 3 .
6 . .
. 9 8
```

Start:

```text
rows = {}
cols = {}
boxes = {}
```

Read:

```text
5
```

Add:

```text
rows[0]

cols[0]

boxes[0]
```

Next:

```text
3
```

Not present.

Add it.

Suppose another

```text
5
```

appears in the same row.

Check:

```text
5 in rows[0]
```

True.

Immediately return:

```text
False
```

# Time Complexity

O(1)

Reason:

The board size is fixed at:

```text
81 cells
```

Each lookup and insertion into a Hash Set is O(1).

Overall:

```text
O(1)
```

(Equivalent to O(81), which is constant.)

# Space Complexity

O(1)

Reason:

The three arrays contain at most:

- 9 row sets
- 9 column sets
- 9 box sets

Their maximum size is fixed.

# Key Learning Points

- Hash Sets are excellent for duplicate detection.
- Validate constraints while traversing instead of checking later.
- Integer division (`//`) is useful for identifying sub-boxes.
- Multiple Hash Sets can independently track different dimensions.
- Early termination improves efficiency.

# Similar Problems

- Sudoku Solver
- Valid Anagram
- Contains Duplicate
- Word Search
- N-Queens

# Interview Takeaway

Whenever a problem asks:

```text
Are there any duplicate values within multiple groups?
```

Think:

```text
Can I maintain a Hash Set for each group?
```

In Sudoku, the groups are:

- Rows
- Columns
- 3×3 Boxes

Tracking all three simultaneously produces a clean and efficient solution.