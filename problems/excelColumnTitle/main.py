'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''

class Solution:
  def convertToTitle(self, n: int) -> str:
    result = ''
    while n > 0:
      x, n = n % 26, n // 26
      if x == 0:
        n -= 1
        result = 'Z' + result
      else:
        result = chr(x + 64) + result
    return result
