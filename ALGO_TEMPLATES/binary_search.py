def binary_searchd(self, array) -> int:
    def condition(value) -> bool:
        pass

    def return_condition() -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2 # // means rownds down and returns whole number
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    
    if return_condition:
        return left
    return -1

"""
* Correctly initialize the boundary variables left and right to specify search space. Only one rule: set up the boundary to include all possible elements;
* Decide return value. Is it return left or return left - 1? Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;
* Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.
"""