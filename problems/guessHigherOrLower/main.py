# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# this works but times out
class Solution:
    def guessNumber(self, n: int) -> int:
        
        direction = guess(n)

        while guess(n) != 0:
            n += direction

        return n



def guess(n):
    return 1 or -1 or 0