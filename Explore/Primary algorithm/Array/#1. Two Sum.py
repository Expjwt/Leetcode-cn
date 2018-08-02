# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arg = sorted(range(len(nums)), key=lambda k: nums[k])
        for i in range(len(arg)):
            for j in range(i + 1, len(nums)):
                temps = nums[arg[i]] + nums[arg[j]]
                if temps == target:
                    return[arg[i],arg[j]]
                if temps > target:
                    break