class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        for x in range(n):
            if 3 ** x > n:
                return False
            if 3 ** x == n:
                return True

        return False

# no loops
# just math
    def _isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        return pow(3, 19) % n == 0



solution = Solution()._isPowerOfThree

test, expected = solution(27), True
print('test:', test, test == expected)
test, expected = solution(0), False
print('test2:', test, test == expected)
test, expected = solution(9), True
print('test3:', test, test == expected)
test, expected = solution(45), False
print('test4:', test, test == expected)