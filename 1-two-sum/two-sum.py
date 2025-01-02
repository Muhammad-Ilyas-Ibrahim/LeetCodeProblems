class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while i != len(nums)-1:
            if nums[i] + nums[j] == target:
                return [i, j]
            if j != len(nums)-1:
                j += 1
            else:
                i += 1
                j = i + 1

