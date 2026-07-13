# Problem Name

424. Longest Repeating Character Replacement

# Difficulty

Medium

# Pattern Used

Sliding Window (Variable Size) + Frequency Counting

# Approach Explanation

### Brute Force

Generate every possible substring.

For each substring:

- Count the frequency of every character.
- Find the character with the highest frequency.
- Calculate how many replacements are needed.
- If the replacements required are less than or equal to `k`, update the answer.

Since every substring must be examined and frequencies are repeatedly calculated, this approach is inefficient.

Time Complexity:

```text
O(n²)
```

or worse depending on how frequencies are computed.

---

### Optimal Approach (Used)

We use a **Variable Sliding Window**.

Maintain:

```text
left
right
```

to represent the current window.

Also maintain a frequency map:

```text
count
```

which stores the frequency of every character inside the window.

Track another variable:

```text
max_freq
```

which stores the highest frequency of any character currently seen.

For every new character:

- Expand the window.
- Update its frequency.
- Update `max_freq`.

The number of replacements needed is:

```text
window_length - max_freq
```

If this value becomes greater than `k`,

the window is no longer valid.

Shrink the window from the left until it becomes valid again.

Keep updating the maximum valid window length.

---

### Why This Works

Inside any window,

the character that appears most frequently does **not** need replacement.

Every other character must be changed.

Therefore,

the number of replacements required is:

```text
window_size - most_frequent_character
```

If this exceeds `k`,

the window cannot be converted into a substring of identical characters.

By shrinking the window only when necessary,

we always maintain the largest valid window.

---

### Why I Used This Pattern

Indicators:

- Need the **longest** valid substring.
- Window size changes dynamically.
- Characters inside the window determine validity.
- Frequency information is required.

These are classic characteristics of a **Variable Sliding Window** problem.

Maintaining character frequencies allows validity checks in constant time.

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

Every character is processed at most twice.

---

### Alternative Version

Instead of using a dictionary,

use an integer array of size:

```text
26
```

Each index represents one uppercase English letter.

Example:

```text
count[ord(char) - ord('A')]
```

Advantages:

- Faster access
- Less hashing overhead

Complexities remain:

Time:

```text
O(n)
```

Space:

```text
O(1)
```

Why is it not used?

A dictionary is easier to understand and works naturally without ASCII calculations.

---

### Walkthrough

Input:

```text
s = "AABABBA"

k = 1
```

Initially:

```text
Window = ""
```

Expand:

```text
"A"

"AA"

"AAB"

"AABA"
```

Current frequencies:

```text
A : 3

B : 1
```

Window size:

```text
4
```

Replacements needed:

```text
4 - 3 = 1
```

Valid.

Expand again:

```text
"AABAB"
```

Window size:

```text
5
```

Maximum frequency:

```text
3
```

Replacements needed:

```text
5 - 3 = 2
```

Too many.

Shrink from the left until:

```text
window_size - max_freq <= k
```

Continue until the string ends.

The largest valid window has length:

```text
4
```

---

# Time Complexity

```text
O(n)
```

Reason:

Each character enters and leaves the sliding window at most once.

---

# Space Complexity

```text
O(1)
```

Reason:

Only character frequencies are stored.

Since there are only 26 uppercase English letters, the extra space is constant.

---

# Key Learning Points

- Variable Sliding Window is useful for finding the longest valid substring.
- Frequency counting helps determine whether a window is valid.
- The most frequent character acts as the anchor for replacements.
- A window is valid when:

```text
window_size - max_frequency <= k
```

- Expand while valid and shrink only when necessary.

---

# Similar Problems

- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Permutation in String
- Find All Anagrams in a String
- Max Consecutive Ones III

---

# Interview Takeaway

Whenever a problem asks:

```text
Find the longest substring after making at most k modifications.
```

Think:

```text
Variable Sliding Window + Frequency Counting
```

A useful observation is that only the **most frequent character** in the current window can remain unchanged. Every other character must be replaced, so checking:

```text
window_size - max_frequency
```

quickly tells whether the current window is valid.