class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = 0
        l = len(nums)-1
        while r <= l :
            curr_index = (r+l) // 2
            if nums[curr_index] == target:
                return curr_index
            # less if statement -> faster speed
            if nums[curr_index] < target:
                r = curr_index + 1
            else:
                l = curr_index - 1     
        return -1