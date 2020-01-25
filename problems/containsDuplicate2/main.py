class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        checked = {}
        for i in range(len(nums)):
            if nums[i] in checked and abs(i - checked[nums[i]]) <= k:
                return True
            checked[nums[i]] = i

        return False


solution = Solution().containsNearbyDuplicate

test, expected = solution([1, 2, 3, 1], 3), True
print('test:', test, test == expected)
test, expected = solution([1, 0, 1, 1], 1), True
print('test2:', test, test == expected)
test, expected = solution([1,2,3,1,2,3], 2), False
print('test3:', test, test == expected)