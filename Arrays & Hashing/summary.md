# LeetCode Patterns Summary

This document summarizes the core ideas, patterns, and interview takeaways from the first set of LeetCode problems solved.

---

# 1. Two Sum

### Pattern

Hash Map

### Core Idea

Store previously seen numbers in a hash map.

For each number:

* Compute the complement (`target - num`).
* Check if the complement already exists.
* If yes, return both indices.
* Otherwise, store the current number.

### Time Complexity

**O(n)**

### Space Complexity

**O(n)**

### Interview Signal

Whenever you need to find **two elements satisfying a condition**, think **Hash Map + Complement**.

---

# 2. Valid Anagram

### Pattern

Frequency Counting (Hash Map)

### Core Idea

Count the frequency of every character in both strings.

If both frequency maps are identical, the strings are anagrams.

### Time Complexity

**O(n)**

### Space Complexity

**O(n)**

### Interview Signal

Whenever **order doesn't matter**, think about comparing **frequencies instead of positions**.

---

# 3. Group Anagrams

### Pattern

Hash Map + Canonical Representation

### Core Idea

Convert every word into a unique key.

Example:

```
eat → aet
tea → aet
ate → aet
```

Use the sorted string as the Hash Map key.

### Time Complexity

**O(n × k log k)**

### Space Complexity

**O(n × k)**

### Better Version

Use a **26-character frequency tuple** as the key.

Time becomes:

```
O(n × k)
```

### Interview Signal

Whenever asked to **group equivalent strings**, generate a **canonical key**.

---

# 4. Contains Duplicate

### Pattern

Hash Set

### Core Idea

Store numbers inside a set.

If a number already exists, return `True`.

### Time Complexity

**O(n)**

### Space Complexity

**O(n)**

### Interview Signal

Need to detect duplicates?

Use a **Hash Set**.

---

# 5. Top K Frequent Elements

### Pattern

Hash Map + Bucket Sort

### Core Idea

1. Count frequencies.
2. Place numbers into buckets according to frequency.
3. Traverse buckets from highest frequency to lowest.

### Time Complexity

**O(n)**

### Space Complexity

**O(n)**

### Alternative

Min Heap

```
O(n log k)
```

### Interview Signal

Whenever you see **Top K Frequent**, think:

1. Frequency Map
2. Heap
3. Bucket Sort (if frequency range is bounded)

---

# 6. Product of Array Except Self

### Pattern

Prefix Product + Suffix Product

### Core Idea

For every index:

```
Answer = Left Product × Right Product
```

Compute:

* Prefix products
* Suffix products

without using division.

### Time Complexity

**O(n)**

### Space Complexity

**O(1)** (excluding output)

### Interview Signal

Whenever you see:

> "Product except current index"

Think:

**Prefix + Suffix**

---

# 7. Longest Consecutive Sequence

### Pattern

Hash Set

### Core Idea

Only begin counting if:

```
num - 1 not in set
```

Then continue forward until the sequence ends.

### Time Complexity

**O(n)**

### Space Complexity

**O(n)**

### Interview Signal

Need consecutive numbers without sorting?

Think:

**Hash Set**

---

# 8. Valid Sudoku

### Pattern

Hash Set

### Core Idea

Maintain three sets:

* Rows
* Columns
* Boxes

If a duplicate appears in any set, the board is invalid.

### Time Complexity

**O(1)**

(Fixed 9×9 board)

### Space Complexity

**O(1)**

### Interview Signal

Need duplicate detection across multiple groups?

Maintain **one Hash Set per group**.

---

# 9. Set Matrix Zeroes

### Pattern

Matrix Traversal + In-place Marking

### Core Idea

Reuse:

* First row
* First column

as marker arrays.

Remember separately whether they originally contained a zero.

### Time Complexity

**O(m × n)**

### Space Complexity

**O(1)**

### Interview Signal

Whenever asked to modify a matrix **in-place**, think:

> Can I reuse part of the matrix as storage?

---

# 10. Rotate Array

### Pattern

Array Reversal

### Core Idea

Reverse:

1. Entire array
2. First `k` elements
3. Remaining elements

### Time Complexity

**O(n)**

### Space Complexity

**O(1)**

### Interview Signal

Whenever an array must be rotated **in-place**, think:

**Three Reversals**

---

# 11. Spiral Matrix

### Pattern

Boundary Traversal

### Core Idea

Maintain:

```
top
bottom
left
right
```

Traverse:

* Left → Right
* Top → Bottom
* Right → Left
* Bottom → Top

Shrink boundaries after every traversal.

### Time Complexity

**O(m × n)**

### Space Complexity

**O(1)**

### Interview Signal

Whenever traversal happens **layer by layer**, think:

**Four Boundaries**

---

# 12. Summary Ranges

### Pattern

Range Tracking

### Core Idea

Track the beginning of the current range.

Whenever consecutive numbers break:

```
nums[i] != nums[i-1] + 1
```

store the completed range.

### Time Complexity

**O(n)**

### Space Complexity

**O(1)**

### Interview Signal

For sorted arrays containing consecutive values, think:

**Track the start and end of each range.**

---

# Pattern Cheat Sheet

| Pattern                     | Problems                                                       |
| --------------------------- | -------------------------------------------------------------- |
| Hash Map                    | Two Sum, Valid Anagram, Group Anagrams, Top K Frequent         |
| Hash Set                    | Contains Duplicate, Longest Consecutive Sequence, Valid Sudoku |
| Frequency Counting          | Valid Anagram, Top K Frequent                                  |
| Prefix & Suffix             | Product of Array Except Self                                   |
| Bucket Sort                 | Top K Frequent                                                 |
| Matrix Traversal            | Set Matrix Zeroes, Spiral Matrix                               |
| In-place Array Manipulation | Rotate Array                                                   |
| Boundary Traversal          | Spiral Matrix                                                  |
| Range Tracking              | Summary Ranges                                                 |

---

# Common Interview Clues

| If you see...            | Think...           |
| ------------------------ | ------------------ |
| Find two numbers         | Hash Map           |
| Detect duplicates        | Hash Set           |
| Compare characters       | Frequency Count    |
| Group similar strings    | Canonical Key      |
| Top K Frequent           | Bucket Sort / Heap |
| Product except self      | Prefix & Suffix    |
| Consecutive sequence     | Hash Set           |
| Validate rows/columns    | Multiple Hash Sets |
| Modify matrix in-place   | Matrix as storage  |
| Rotate array in-place    | Three Reversals    |
| Spiral traversal         | Four Boundaries    |
| Sorted consecutive array | Range Tracking     |

---

# Overall Learning

From these 12 problems, the most important patterns learned are:

* Hash Maps for fast lookups
* Hash Sets for duplicate detection
* Frequency Counting
* Prefix & Suffix techniques
* Bucket Sort
* In-place array manipulation
* Matrix traversal
* Boundary simulation
* Range tracking

These patterns form the foundation for solving a large number of array, string, and matrix problems in coding interviews.
