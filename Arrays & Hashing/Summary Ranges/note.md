# Problem Name

228. Summary Ranges

# Difficulty

Easy

# Pattern Used

Array Traversal (Two Pointers / Range Tracking)

# Approach Explanation

### Brute Force

For every number:

- Check the next number.
- Continue while numbers are consecutive.
- Record the current range.
- Repeat for the remaining elements.

This idea works but can become messy if indices are not managed carefully.

---

### Optimal Approach (Used)

Since the array is already:

- Sorted
- Unique

we only need to detect where a consecutive sequence breaks.

Maintain one variable:

```text
start
```

which stores the beginning of the current range.

Traverse the array:

If

```text
nums[i] == nums[i-1] + 1
```

the range continues.

Otherwise:

- The current range ends.
- Add it to the answer.
- Start a new range.

After the loop, don't forget to add the final range.

---

### Why This Works

Because the array is sorted, consecutive numbers always appear together.

Whenever the difference between adjacent numbers is greater than one,

```text
nums[i] != nums[i-1] + 1
```

the previous range has ended.

Each range is processed exactly once.

---

### Why I Used This Pattern

Indicators:

- Input array is already sorted.
- Need to group consecutive values.
- Only one traversal is required.
- No extra data structures are necessary.

This is a classic range-tracking problem.

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

(extra space excluding the output list)

This is optimal.

Reason:

Every number must be inspected at least once.

---

### Alternative Version

Use two pointers:

```text
left
right
```

Move `right` while numbers remain consecutive.

When the sequence ends:

- Record the range.
- Move both pointers to the next sequence.

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

Both approaches have the same complexity.

Tracking only the start of the range is simpler and requires fewer variables.

---

### Walkthrough

Input:

```text
[0,1,2,4,5,7]
```

Start:

```text
start = 0
```

Sequence:

```text
0 → 1 → 2
```

Break at:

```text
4
```

Add:

```text
"0->2"
```

New range:

```text
4 → 5
```

Break at:

```text
7
```

Add:

```text
"4->5"
```

Last range:

```text
7
```

Add:

```text
"7"
```

Final result:

```text
["0->2","4->5","7"]
```

# Time Complexity

O(n)

Reason:

The array is traversed exactly once.

# Space Complexity

O(1)

Reason:

Only a few variables are used.

The output list is not counted as extra space.

# Key Learning Points

- Sorted arrays often require only one traversal.
- Detect the end of a range by checking adjacent elements.
- Remember to process the final range after the loop.
- Track only the information you need—in this case, the start of the current range.
- Consecutive sequence problems often reduce to simple comparisons.

# Similar Problems

- Merge Intervals
- Insert Interval
- Missing Ranges
- Longest Consecutive Sequence
- Remove Duplicates from Sorted Array

# Interview Takeaway

Whenever a problem involves:

```text
A sorted array with consecutive values.
```

Think:

```text
Can I identify where a sequence starts and ends?
```

Range tracking with a single traversal is often the simplest and most efficient solution.