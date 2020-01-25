/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    
  var checked = {};
  
  for (var i = 0; i < nums.length; i++) {
      const num = nums[i].toString();
      if (checked[num]) {
          return true;
      }
      checked[num] = true;
  }
  
  return false;
  
};