# Problem Name

128. Longest Consecutive Sequence

# Difficulty

Medium

# Pattern Used

Hash Set

# Approach Explanation

### Brute Force

For every number:

- Search for the next consecutive number.
- Continue until the sequence ends.
- Keep track of the maximum length.

Example:

nums = [100,4,200,1,3,2]

Starting from 1:

1 → 2 → 3 → 4

Length = 4

Starting from 2:

2 → 3 → 4

Length = 3

This repeats many unnecessary searches.

Why not use this?

- Searching each next element repeatedly is expensive.
- Time Complexity becomes O(n²).

---

### Better Approach

Sort the array first.

Example:

nums = [100,4,200,1,3,2]

After sorting:

[1,2,3,4,100,200]

Traverse once and count consecutive numbers.

Why not use it?

Time Complexity:

O(n log n)

The problem explicitly asks for an O(n) solution.

---

### Optimal Approach (Used)

Store every number inside a Hash Set.

A sequence should only start if the previous number does not exist.

Condition:

```text
num - 1 not in num_set
```

If true:

Keep checking:

```text
num + 1
num + 2
num + 3
...
```

until the sequence ends.

Example:

nums = [100,4,200,1,3,2]

Hash Set:

```text
{100,4,200,1,3,2}
```

Start checking:

100

99 doesn't exist

Sequence:

100

Length = 1

---

4

3 exists

Skip.

Reason:

This sequence was already counted starting from 1.

---

200

199 doesn't exist

Sequence:

200

Length = 1

---

1

0 doesn't exist

Sequence:

1 → 2 → 3 → 4

Length = 4

Return:

```text
4
```

---

### Why This Works

Every consecutive sequence has exactly one starting point.

Example:

```text
1 2 3 4
```

Only `1` has no previous number.

By only starting from numbers whose predecessor is missing,

```text
num - 1 not in set
```

each sequence is visited exactly once.

No duplicate work occurs.

---

### Why I Used This Pattern

Indicators:

- Fast lookup required.
- Order of the input does not matter.
- Need O(n) complexity.
- Consecutive existence checks.

Hash Sets provide:

- O(1) average lookup
- O(1) insertion

making them ideal.

---

### Could There Be A Better Version?

Current solution:

Time:

O(n)

Space:

O(n)

This is already optimal.

Reason:

Every element must be inspected at least once.

Sorting cannot satisfy the required complexity.

---

### Alternative Version

Sort first.

Example:

```text
nums.sort()
```

Traverse while counting consecutive values.

Complexities:

Time:

O(n log n)

Space:

O(1)

Why is it worse?

Sorting dominates the running time.

The problem specifically requires O(n).

---

### Walkthrough

Input:

```text
nums = [100,4,200,1,3,2]
```

Hash Set:

```text
{100,4,200,1,3,2}
```

Start:

100

Length = 1

---

4

Previous number exists (3)

Skip.

---

200

Length = 1

---

1

Sequence:

```text
1 → 2 → 3 → 4
```

Length = 4

Maximum:

```text
4
```

Return:

```text
4
```

# Time Complexity

O(n)

Reason:

- Building the Hash Set takes O(n).
- Each number is visited at most once while extending sequences.

Overall:

```text
O(n)
```

# Space Complexity

O(n)

Reason:

The Hash Set stores every unique number.

# Key Learning Points

- Hash Sets are excellent for O(1) lookups.
- Only begin counting from the start of a sequence.
- Avoid repeating work by skipping numbers with predecessors.
- Sorting is not always the optimal choice.
- Detecting sequence starts is the key optimization.

# Similar Problems

- Contains Duplicate
- Longest Increasing Subsequence
- Number of Islands
- Top K Frequent Elements
- Missing Number

# Interview Takeaway

Whenever you see:

```text
Longest consecutive...
```

Think:

```text
Can I use a Hash Set for O(1) lookup?
```

Then ask:

```text
How can I avoid recounting the same sequence?
```

Answer:

Only start when:

```text
num - 1 not in set
```

This simple observation reduces the solution from **O(n²)** or **O(n log n)** to **O(n)**.