class Solution:

    def isPowerOfFour(self, num: int) -> bool:
        
        for x in range(num):
            result = 4 ** x
            if result > num:
                return False
            if result == num:
                return True

        return False

    def _isPowerOfFour(self, num: int) -> bool:
        
        while num % 4 == 0:
            num /= 4
        
        return num == 1