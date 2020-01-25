'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

# this solution works but the time limit is exceeded almost always lololol
class Solution:
  def removeDuplicates(self, nums: [int]) -> int:
    '''
    remove each element, 
    if it still exists, move onto the next one, 
    if not, put it tf back in
    '''
    print('input:', nums)
    i = 0
    while i < len(nums):
      num = nums.pop(i)
      if num not in nums: # probably times out becuase of this 
        nums.insert(0, num)
      else:
        print('removed:', num)
        i += 1
    print('result:', nums)
    return len(nums)

# a little different than my solution but does not time out
def not_jeds_removeDuplicates(self, nums: [int]) -> int:
  i = 0
  while i < len(nums) - 1:
    if nums[i] == nums[i + 1]:
      del nums[i]
    else:
      i += 1
  return len(nums)


nums = [1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6]
nums = sorted(nums)
test = Solution().removeDuplicates(nums)
print('test result:', test)