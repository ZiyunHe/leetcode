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