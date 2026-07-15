# Problem Name

438. Find All Anagrams in a String

# Difficulty

Medium

# Pattern Used

Fixed Sliding Window + Frequency Counting

# Approach Explanation

### Brute Force

Generate every substring of `s` having length equal to `p`.

For every substring:

- Sort the substring.
- Sort `p`.
- Compare both.

If they are equal, record the starting index.

Time Complexity:

```text
O((n - m + 1) × m log m)
```

where

```text
n = len(s)

m = len(p)
```

Sorting every substring is inefficient.

---

### Optimal Approach (Used)

Since an anagram has:

- the same characters
- with the same frequencies

we only need to compare character frequencies.

Maintain two frequency arrays:

```text
p_count
```

Stores the frequency of characters in `p`.

```text
window_count
```

Stores the frequency of the current window in `s`.

The window size always remains:

```text
len(p)
```

Steps:

- Build the frequency arrays for the first window.
- Compare both arrays.
- Slide the window one character at a time.
- Add the incoming character.
- Remove the outgoing character.
- Compare the frequency arrays again.
- If equal, record the window's starting index.

---

### Why This Works

Every anagram has exactly the same frequency of each character.

The order of characters does not matter.

By maintaining a fixed-size sliding window, we avoid recalculating frequencies from scratch.

Only two characters change when the window moves:

- One enters.
- One leaves.

This makes the solution efficient.

---

### Why I Used This Pattern

Indicators:

- Need to examine every substring of fixed length.
- Character frequencies determine validity.
- Order of characters is irrelevant.
- Repeated frequency calculations should be avoided.

These are classic signs of a **Fixed Sliding Window + Frequency Counting** problem.

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

The frequency arrays always have a fixed size of 26.

---

### Alternative Version

Use Python's `Counter`.

Example:

```python
Counter(window) == Counter(p)
```

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

Although `Counter` makes the code shorter, comparing dictionaries has more overhead.

Using arrays of size 26 is faster and is commonly preferred in coding interviews.

---

### Walkthrough

Input:

```text
s = "cbaebabacd"

p = "abc"
```

Window size:

```text
3
```

First window:

```text
"cba"
```

Frequency matches:

```text
"abc"
```

Record:

```text
0
```

Slide window.

Window:

```text
"bae"
```

Not an anagram.

Continue sliding.

Window:

```text
"bac"
```

Frequency matches again.

Record:

```text
6
```

Final answer:

```text
[0,6]
```

---

# Time Complexity

```text
O(n)
```

Reason:

Each character enters and leaves the sliding window exactly once.

Frequency array comparison is constant time because the array size is always 26.

---

# Space Complexity

```text
O(1)
```

Reason:

Two frequency arrays of fixed size 26 are maintained.

The extra space does not depend on the input size.

---

# Key Learning Points

- Fixed Sliding Window is useful when the substring length is predetermined.
- Character frequencies are more useful than sorting for anagram problems.
- Only update the incoming and outgoing characters when the window moves.
- Arrays are more efficient than hash maps when the character set is fixed.
- Comparing frequency arrays is constant time for lowercase English letters.

---

# Similar Problems

- Permutation in String
- Minimum Window Substring
- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Valid Anagram

---

# Interview Takeaway

Whenever a problem asks:

```text
Find every substring that is an anagram or permutation of another string.
```

Think:

```text
Fixed Sliding Window + Frequency Counting
```

Instead of sorting every substring, maintain a frequency array for the current window. As the window slides, update only the incoming and outgoing characters, reducing the solution from quadratic time to linear time.