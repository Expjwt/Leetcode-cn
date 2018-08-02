# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        i = 0
        flag = True
        while (flag):
            digits[i] += 1
            flag, digits[i] = self.check(digits[i])
            i += 1
            if i == len(digits) and flag:
                digits.append(1)
                break
        digits.reverse()
        return digits

    def check(self, decimal):
        if decimal >= 10:
            return True, decimal - 10
        else:
            return False, decimal