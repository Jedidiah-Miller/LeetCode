class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return True

        for x in range(num):
            y = x ** 2
            if y == num:
                return True
            if y > num:
                return False

# not mine
# one liner
    def _isPerfectSquare(self, num: int) -> bool:
        return int(num ** 0.5) ** 2 == num

solution = Solution()._isPerfectSquare

test, expected = solution(16), True
print(test, test == expected)
test, expected = solution(14), False
print(test, test == expected)
test, expected = solution(1), True
print(test, test == expected)