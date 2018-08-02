# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = []
        j = 0
        i = 0
        while j < len(nums1):
            while i < len(nums2):
                if nums2[i] == nums1[j]:
                    inter.append(nums2[i])
                    del nums1[j],nums2[i]
                    if nums1 == [] or nums2 == []:
                        break
                    i -= 1
                    j -= 1
                i += 1
            i = 0
            j += 1
        return inter