class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub_map = {}
        for i in range(len(nums)):
            if nums[i] in sub_map:
                return [sub_map[nums[i]], i]
            else:
                sub_num = target - nums[i]
                sub_map[sub_num] = i
        return [-1, -1]