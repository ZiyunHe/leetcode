class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(nums,start,end):
            if start>end:
                return -1
            
            mid = start + (end-start)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                return binarySearch(nums,start,mid-1)
            else:
                return binarySearch(nums,mid+1,end)
            
            
        indx = binarySearch(nums,0,len(nums)-1)
        
        if indx == -1:
            return [-1,-1]
        left_most = indx
        right_most = indx
        
        while True:
            indx = binarySearch(nums,0,indx-1)
            
            if indx == -1:
                break
                
            left_most = indx
        while True:
            indx = binarySearch(nums,right_most+1,len(nums)-1)
            
            if indx == -1:
                break
            
            right_most = indx
        return [left_most,right_most]