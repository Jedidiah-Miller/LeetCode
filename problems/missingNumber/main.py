class Solution:
    # mine
    def missingNumber(self, nums: [int]) -> int:
        numSet = set(nums)
        for n in range(0, len(nums) + 1):
            if n not in numSet: return n

    # not mine, this one is clever tho
    # it is slower
    def missing_number(self, nums: [int]) -> int:
        n = len(nums)
        return (n * (n + 1) / 2) - sum(nums)