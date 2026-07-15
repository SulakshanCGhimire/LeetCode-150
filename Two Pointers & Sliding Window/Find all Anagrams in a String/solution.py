"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

Example 1:

    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
    
Example 2:

    Input: s = "abab", p = "ab"
    Output: [0,1,2]
    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
 
Constraints:

    1 <= s.length, p.length <= 3 * 104
    s and p consist of lowercase English letters.
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)

        Since the strings contain only lowercase English letters,
        the frequency arrays have a fixed size of 26.
        """

        if len(p) > len(s):
            return []

        result = []

        p_count = [0] * 26
        window_count = [0] * 26

        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            window_count[ord(s[i]) - ord('a')] += 1

        if p_count == window_count:
            result.append(0)

        left = 0

        for right in range(len(p), len(s)):
            window_count[ord(s[right]) - ord('a')] += 1
            window_count[ord(s[left]) - ord('a')] -= 1
            left += 1

            if p_count == window_count:
                result.append(left)

        return result
