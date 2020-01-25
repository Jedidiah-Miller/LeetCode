class Solution:
    # not mine
    def rob(self, nums: [int]) -> int:
        x, y = 0, 0

        for n in nums:
            x, y = n+ y, max(x, y)

        return max(x, y)