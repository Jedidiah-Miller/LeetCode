'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
    [-1, 0, 1],
    [-1, -1, 2]
]
'''

from itertools import combinations

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:

        result = []
        obj = {}

        for combo in combinations(nums, 3):
            if sum(combo) == 0:
                combo = sorted(combo)
                if not combo in result:
                    result.append(combo)
                string = str(combo)
                obj[string] = combo

        return [obj[x] for x in obj]


    def _threeSum(self, nums: [int]) -> [[int]]:

        length = len(nums)
        result = []

        for i in range(length - 2):
            for j in range(length - 1):
                if i == j:
                    continue
                for k in range(length):
                    if i == k or j == k:
                        continue
                    arr = sorted([nums[i], nums[j], nums[k]])
                    if sum(arr) == 0:
                        if arr not in result:
                            result.append(arr)

        return result


testList = [-11,-3,-6,12,-15,-13,-7,-3,13,-2,-10,3,12,-12,6,-6,12,9,-2,-12,14,11,-4,11,-8,8,0,-12,4,-5,10,8,7,11,-3,7,5,-3,-11,3,11,-13,14,8,12,5,-12,10,-8,-7,5,-9,-11,-14,9,-12,1,-6,-8,-10,4,9,6,-3,-3,-12,11,9,1,8,-10,-3,2,-11,-10,-1,1,-15,-6,8,-7,6,6,-10,7,0,-7,-7,9,-8,-9,-9,-14,12,-5,-10,-15,-9,-15,-7,6,-10,5,-7,-14,3,8,2,3,9,-12,4,1,9,1,-15,-13,9,-14,11,9]

test = Solution().threeSum(testList)
print('test:', test)