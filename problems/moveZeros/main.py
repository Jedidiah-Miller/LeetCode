# this is supposed to return None
# but for testing purposes I returned the list

class Solution:
    # my solution
    def moveZeroes(self, nums: [int]) -> [int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        while count < len(nums):

            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1

            count += 1

        return nums


    # not mine but I like it more than mine
    # I wrote the notes to understand it better
    def move_zeros(self, nums: [int]) -> [int]:

        z = 0 # keep track of the last 0 we've seen

        for i in range(len(nums)):
            if nums[i] != 0:
                if i != z: # only swap if needed, improves speed
                    # swap the values of nums i and z if nums i is not 0
                    nums[i], nums[z] = nums[z], nums[i]
                # increment z by one so that way we know which value to swap with nums[i]
                # we don't swap until i != i
                z += 1
            # if z is not incremented, the z index is a 0
            # nums[z] == 0 and needs to be swapped with nums[i]
        
        return nums


solution = Solution().moveZeroes

test, expected = solution([0, 1, 0, 3, 12]), [1,3,12,0,0]
print('test:', test, test == expected)
test2, expected2 = solution([0, 1, 0, 3, 12, 0, 0, 0, 0, 0, 1, 4, 6, 2, 8, 9, 999, 664, 25, 0]), [1, 3, 12, 1, 4, 6, 2, 8, 9, 999, 664, 25, 0, 0, 0, 0, 0, 0, 0, 0]
print('test2:', test2, test2 == expected2)