class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        for x in range(n):
            if 2 ** x > n:
                return False
            if 2 ** x == n:
                return True

        return False



solution = Solution().isPowerOfTwo

test, expected = solution(1), True
print('test:', test, test == expected)
test, expected = solution(16), True
print('test2:', test, test == expected)
test, expected = solution(218), False
print('test3:', test, test == expected)
test, expected = solution(65535), False
print('test4:', test, test == expected)