class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = float('-inf')
        curr_max = 0
        for num in nums:
            curr_max += num
            if curr_max > res:
                res = curr_max
            if curr_max < 0:
                curr_max = 0
        return res

# 这个答案的想法：
# 从头到尾过一遍
# 加上当前数
# 如果数大于历史记录里的最大值
# 覆盖历史记录的最大值
# 如果小于 那就清零从头来