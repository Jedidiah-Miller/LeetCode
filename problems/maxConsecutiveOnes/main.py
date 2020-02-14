class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = maxOnes = 0

        for n in nums:
            if n == 1:
                count += 1
            else:
                if count > maxOnes:
                    maxOnes = count
                count = 0

        return maxOnes if maxOnes > count else count