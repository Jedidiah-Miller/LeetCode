'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''


class Solution:
  #  this is mine, it kept timing out
  def strStr(self, haystack: str, needle: str) -> int:
    if len(needle) < 1:
      return 0

    for i in range(len(haystack)):
      for j in range(len(haystack)):
        test_needle = haystack[i if i == j else i:j]
        # this does not include the last char
        if test_needle == needle:
          print('found:', test_needle)
          return i
    return -1

# somone elses solution
  def _strStr(self, haystack: str, needle: str) -> int:
    if len(haystack) < len(needle):
      return -1
    for i in range(len(haystack)-(len(needle)-1)):
      if haystack[i:i+len(needle)] == needle:
        return i
    if i == len(haystack)-len(needle):
      return -1


haystack = "a"
needle = "a"

test = Solution().strStr(haystack, needle)
print('result:', test)