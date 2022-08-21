class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {0: nums[0]}
        for i in range(1, len(nums)):
            cache[i] = nums[i] + cache[i - 1] if cache[i - 1] > 0  else nums[i]
        return max(cache.values())

# 按照答案写的