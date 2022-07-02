# best solution for time
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # ONE-PASS HASH TABLE
    # TIME: O(n)
    # SPACE: O(n)
    hashmap = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in hashmap:
            return [i, hashmap[difference]]
        
        hashmap[nums[i]] = i

# best solution for less memory
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]