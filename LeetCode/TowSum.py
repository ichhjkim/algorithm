from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums = [[nums[i], i] for i in range(len(nums))]

        nums.sort()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i][0]+nums[j][0]) == target:
                    return [nums[i][1], nums[j][1]]

'''
One-pass Hash Table

    def twoSum(self, nums, target):

        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
'''
