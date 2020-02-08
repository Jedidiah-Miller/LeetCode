class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for x in nums1:
            if x in result:
                continue
            if x in nums2:
                result.append(x)

        return result


    # not mine
    def _intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)