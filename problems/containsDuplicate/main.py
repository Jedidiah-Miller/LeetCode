class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        checked = {}
        for x in nums:
            strX = str(x)
            if strX in checked:
                return True
            checked[strX] = True

        return False


solution = Solution().containsDuplicate

test, expected = solution([1, 2, 3, 1]), True
print('test:', test, test == expected)