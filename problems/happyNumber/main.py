class Solution:
    def isHappy(self, n: int) -> bool:
        
        checked = []

        while n != 1 and n not in checked:
            checked.append(n)
            strNum = str(n)
            n = 0

            for num in strNum:
                n += int(num) **2

        return n == 1


solution = Solution().isHappy

test, expected = solution(19), True
print('test:', test, test == expected)