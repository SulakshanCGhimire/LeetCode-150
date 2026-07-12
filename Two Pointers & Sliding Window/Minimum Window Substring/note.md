# Problem Name

76. Minimum Window Substring

# Difficulty

Hard

# Pattern Used

Sliding Window + Hash Map (Variable Size Window)

# Approach Explanation

### Brute Force

Generate every possible substring of `s`.

For every substring:

- Count its characters.
- Check whether it contains every character of `t`.
- Keep the smallest valid substring.

Since there are many substrings and each validation requires checking character frequencies, this approach becomes extremely slow.

Time Complexity:

```text
O(m² × n)
```

which exceeds the limits.

---

### Optimal Approach (Used)

Use a **variable-size Sliding Window**.

Maintain two frequency maps:

```text
need
```

Stores the required frequency of every character in `t`.

```text
window
```

Stores the frequency of characters inside the current window.

Also maintain two variables:

```text
have
```

Number of character requirements currently satisfied.

```text
need_count
```

Total number of unique characters that must be satisfied.

Expand the window by moving the right pointer.

Whenever every required character is present,

```text
have == need_count
```

the window is valid.

Now shrink the window from the left as much as possible while keeping it valid.

Update the smallest window whenever a shorter valid window is found.

---

### Why This Works

The window grows until it satisfies every required character.

Once valid, making it smaller may produce a better answer.

Instead of checking every substring independently, the window dynamically expands and contracts.

Every character enters and leaves the window at most once.

This gives a linear-time solution.

---

### Why I Used This Pattern

Indicators:

- Need the **smallest** valid substring.
- Substring must be continuous.
- Character frequencies matter.
- Window size is not fixed.
- Need to dynamically expand and shrink.

These are classic signs of a **Variable Sliding Window** problem.

Frequency maps efficiently keep track of whether the current window satisfies all requirements.

---

### Could There Be A Better Version?

Current solution:

Time:

```text
O(m + n)
```

Space:

```text
O(k)
```

where

```text
k
```

is the number of unique characters.

This is optimal.

Every character must be processed at least once.

---

### Alternative Version

Instead of dictionaries (`Counter` and `dict`),

use two arrays of size:

```text
128
```

for ASCII characters.

Each character's ASCII value is used as its index.

Example:

```text
count[ord('A')]
```

Advantages:

- Faster lookup
- Less hashing overhead

Complexities remain:

Time:

```text
O(m + n)
```

Space:

```text
O(1)
```

Why is it not used?

Using dictionaries makes the solution easier to understand and works naturally with any character set.

---

### Walkthrough

Input:

```text
s = "ADOBECODEBANC"

t = "ABC"
```

Required frequency:

```text
A : 1

B : 1

C : 1
```

Expand the window.

Eventually:

```text
ADOBEC
```

contains all required characters.

Current answer:

```text
"ADOBEC"
```

Now shrink the window.

Remove unnecessary characters from the left.

Continue expanding and shrinking.

Later the window becomes:

```text
"BANC"
```

Still contains:

```text
A

B

C
```

Length:

```text
4
```

No smaller valid window exists.

Return:

```text
"BANC"
```

---

# Time Complexity

```text
O(m + n)
```

Reason:

Each character enters and leaves the sliding window at most once.

---

# Space Complexity

```text
O(k)
```

Reason:

Two frequency maps are maintained.

The extra space depends on the number of unique characters being tracked.

---

# Key Learning Points

- Variable-size Sliding Window is used when finding the smallest or largest valid substring.
- Frequency maps efficiently track required characters.
- Expand until the window becomes valid.
- Shrink while the window remains valid.
- Maintain only the necessary information instead of repeatedly checking every substring.

---

# Similar Problems

- Permutation in String
- Find All Anagrams in a String
- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Minimum Size Subarray Sum

---

# Interview Takeaway

Whenever a problem asks:

```text
Find the minimum or maximum contiguous substring satisfying certain conditions.
```

Think:

```text
Variable Sliding Window
```

If the validity of a window depends on character frequencies, combine the Sliding Window with a Hash Map or Counter to efficiently maintain the required counts. This approach often reduces a quadratic solution to linear time.