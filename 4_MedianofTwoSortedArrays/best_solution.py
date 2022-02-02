"""
binary search problem
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A # A is the shorter one
        
        lenA, lenB = len(A), len(B)
        total = lenA + lenB
        half = total // 2
        
        l, r = 0, lenA - 1
        while True:
            i = l + (r - l) // 2 # index in A 
            j = half - i - 2 
            
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if i+1 < lenA else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if j+1 < lenB else float('inf')
            
            if Aleft <= Bright and Aright >= Bleft:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            
            elif Aright < Bleft:
                l = i + 1
            else:
                r = i - 1