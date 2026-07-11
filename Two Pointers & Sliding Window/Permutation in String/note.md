# Problem Name

567. Permutation in String

# Difficulty

Medium

# Pattern Used

Sliding Window + Hash Map (Frequency Counter)

# Approach Explanation

### Brute Force

Generate every possible substring of `s2` having length equal to `s1`.

For every substring:

- Generate all permutations and compare with `s1`.

or

- Sort both strings and compare.

Although correct, generating permutations is extremely expensive.

Even sorting every substring results in:

Time Complexity:

```text
O((n - m + 1) × m log m)
```

where

- `n = len(s2)`
- `m = len(s1)`

This is too slow for the given constraints.

---

### Optimal Approach (Used)

A permutation contains:

- the same characters
- with the same frequencies

Instead of checking every permutation, compare **character frequencies**.

Maintain two frequency maps:

```text
need
```

Stores the frequency of characters in `s1`.

```text
window
```

Stores the frequency of the current window inside `s2`.

The window size is always equal to:

```text
len(s1)
```

Move the window one character at a time.

For every movement:

- Add the new character.
- Remove the leftmost character if the window becomes too large.
- Compare both frequency maps.

If they become equal,

return:

```text
True
```

Otherwise continue until the end.

---

### Why This Works

A permutation simply rearranges characters.

Therefore,

if two strings have exactly the same frequency of every character,

they are permutations of each other.

The sliding window ensures we only inspect substrings whose length equals `s1`.

Each character enters and leaves the window exactly once.

---

### Why I Used This Pattern

Indicators:

- Need to check every substring of fixed size.
- Character frequencies matter.
- Order does **not** matter.
- Efficient repeated checking is required.

Whenever a problem asks whether a substring is an anagram or permutation of another string,

Sliding Window + Frequency Counting is usually the best approach.

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

Since only lowercase English letters are used, the frequency map size never exceeds 26.

This is optimal.

---

### Alternative Version

Instead of using `Counter`, use two integer arrays of size:

```text
26
```

Each index represents one lowercase letter.

Example:

```text
index 0 -> a

index 1 -> b

...

index 25 -> z
```

Updating arrays is faster than updating hash maps.

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

`Counter` makes the implementation cleaner and easier to understand.

The array implementation is slightly faster and is often preferred in interviews.

---

### Walkthrough

Input:

```text
s1 = "ab"

s2 = "eidbaooo"
```

Frequency of `s1`:

```text
{
a : 1,
b : 1
}
```

Start sliding window of size 2.

Window:

```text
"ei"
```

Not equal.

Move window.

```text
"id"
```

Not equal.

Move again.

```text
"db"
```

Not equal.

Move again.

```text
"ba"
```

Window frequency:

```text
{
a : 1,
b : 1
}
```

Matches the required frequency.

Return:

```text
True
```

---

# Time Complexity

```text
O(n)
```

Reason:

Each character enters and leaves the sliding window exactly once.

---

# Space Complexity

```text
O(1)
```

Reason:

Only character frequency maps are maintained.

Since there are only 26 lowercase English letters, the extra space is constant.

---

# Key Learning Points

- Sliding Window works well for fixed-size substring problems.
- Frequency maps are useful when character order is irrelevant.
- Compare character counts instead of generating permutations.
- Every window shift updates only two characters.
- Fixed alphabet size often allows constant extra space.

---

# Similar Problems

- Find All Anagrams in a String
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Longest Repeating Character Replacement
- Valid Anagram

---

# Interview Takeaway

Whenever a problem asks:

```text
Does one string contain an anagram or permutation of another?
```

Think:

```text
Fixed-size Sliding Window + Frequency Counting
```

If the substring length is fixed, maintain a moving window and compare character frequencies instead of recomputing them from scratch. This reduces the solution from quadratic time to linear time.