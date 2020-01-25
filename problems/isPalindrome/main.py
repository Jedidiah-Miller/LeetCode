class Solution:
    def isPalindrome(self, s: str) -> bool:
        testString = ''
        for x in s:
            if x.isalnum():
                testString += x.lower()
        return testString == testString[::-1]


solution = Solution().isPalindrome

test, expected = solution("A man, a plan, a canal: Panama"), True
print('test:', test, test == expected)
test2, expected2 = solution("race a car"), False
print('test2:', test2, test2 == expected2)