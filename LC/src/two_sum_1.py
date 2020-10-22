class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in nums:
                idx2 = nums.index(diff)
                if idx != idx2:
                    return sorted([idx, nums.index(diff)])
