'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''

class Solution:
  def titleToNumber(self, s: str) -> int:
    # there will be a maximum of two letters
    # if there are two
      # take the second one, and find the number for it
      # take the first one and mulitply the regular corresponding number by 26
      # ex: AA would be 27
      # the second A would be 1
      # the first A would be 26 times 1, so 26
      # for a total of 26 + 1
    if len(s) > 1:
      y = ord(s[1]) - 64
      x = (ord(s[0]) - 64) * y
      return x + y
    else:
      return ord(s) - 64