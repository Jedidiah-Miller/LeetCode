from itertools import combinations

class Solution:
    def climbStairs(self, n: int) -> int:

        a = b = 1

        for _ in range(n - 1):
            print(a, b)
            temp = a + b
            a = b
            b = temp
        return b


solution = Solution().climbStairs

test, expected = solution(2), 2
print('test:', test, test == expected)
test2, expected2 = solution(3), 3
print('test2:', test2, test2 == expected2)