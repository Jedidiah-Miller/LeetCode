'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''


class Solution:
    # my first attempt, not complete
    def plusOne(self, digits: [int]) -> [int]:
        # work backwards
        for i in range(len(digits)):
            # start by checking the last digit
            # if it is not 9, then we just need to add one
            # and we're done
            # if it is 9 then we need to worry about the next digit
            # it is possible that we just end up adding another int to the list
            # ex 99, 999, 9999
            if digits[len(digits) - i - 1] == 9:
                print('doing the math')
                # change it to 0
                # add 1 to the next digit
                digits[len(digits) - i - 1] = 0
                digits[len(digits) - i - 2] += 1
            else:
                digits[len(digits) - i - 1] += 1
                break
        return digits

    # also mine but a shorter version
    # lazy af version
    # much typecasting
    # idk the time complexity but it can't be good
    # it's like 2 or 3 n
    def _plusOne(self, digits: [int]) -> [int]:
        return [int(x) for x in str(int(''.join([str(x) for x in digits])) + 1)]


    # not mine, but definetly the proper way of doing it
    def __plusOne(self, digits: [int]) -> [int]:
        flag = 0
        i = len(digits)
        while flag == 0:
            i = i - 1
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                flag = 1
            elif digits[i] == 9:
                digits[i] = 0
                if not digits[i - 1]:
                    digits[i] = 1
                    digits.append(0)
                    flag = 1
        return digits
