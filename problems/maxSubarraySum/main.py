'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        if len(nums) < 2:
            return nums[0]
        result = nums[0]

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subArr = nums[i:j]
                subArrSum = sum(subArr)
                if subArrSum > result:
                    result = subArrSum

        return result


nums = [-1]
test = Solution().maxSubArray(nums)

print(f'result: {test}')