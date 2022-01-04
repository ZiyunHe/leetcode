class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<nums[r]:
                if nums[mid]<target<=nums[r]:
                    l = mid+1
                else:
                    r = mid
            else:
                if nums[l]<=target<nums[mid]:
                    r = mid
                else:
                    l = mid+1
        return -1

# with explaination
# class Solution:
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             # if found target value, return the index
#             if nums[mid] == target:
#                 return mid
            
#             # determine it's left rotated or right rotated
#             """
#             No rotated:
#             1 2 3 4 5 6 7
#                  mid
                 
#             left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
#             3 4 5 6 7 1 2
#                  mid
#             search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side
            
#             right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
#             6 7 1 2 3 4 5
#                  mid          
#             search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
#             """
#             if nums[mid] >= nums[left]: # left rotated
#                 # in ascending order side
#                 if nums[left] <= target and target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             else: # right rotated
#                 # in ascending order side
#                 if nums[mid] < target and target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         # cannot find the target value
#         return -1

# best solution similar to my first idea
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         def helper(a):
#             lo = 0
#             hi = len(a)-1
#             while lo<hi:
#                 mid = (lo+hi)//2
#                 if nums[mid]<=nums[hi]:
#                     hi=mid
#                 else:
#                     lo=mid+1
#             mid=(lo+hi)//2
#             print(mid, lo, hi)
#             return mid
#         def findTarget(a,lo, hi, target):
#             while lo< hi:
#                 mid = (lo+hi)//2
#                 if a[mid]>=target:
#                     hi = mid
#                 else:
#                     lo = mid+1
#             mid = (hi+lo)//2
#             return mid
#         mid = helper(nums)
#         i = findTarget(nums,0,mid-1,target)
#         j = findTarget(nums,mid,len(nums)-1,target)
#         print(mid,i,j)
#         if nums[j]==target:
#             return j
#         elif mid>0 and nums[i]==target:
#             return i
            
#         return -1