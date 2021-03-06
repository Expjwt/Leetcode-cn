# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        try:
            for i in range(0,len(nums),2):
                if i+1 < len(nums):
                    if nums[i] != nums[i + 1]:
                        return nums[i]
                else:
                    return nums[-1]
        except:
            return nums[0]