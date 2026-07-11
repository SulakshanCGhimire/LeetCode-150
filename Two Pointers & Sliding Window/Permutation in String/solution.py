"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").
    
Example 2:

    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false
 
Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            Time Complexity: O(n)
            Space Complexity: O(1)

            n = len(s2)

            Since the strings contain only lowercase English letters,
            the character set size is fixed (26).
        """

        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter()

        left = 0

        for right in range(len(s2)):
            window[s2[right]] += 1

            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

            if window == need:
                return True

        return False