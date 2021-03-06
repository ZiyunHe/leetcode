Most Generalized Binary Search
Suppose we have a search space. It could be an array, a range, etc. Usually it's sorted in ascend order. For most tasks, we can transform the requirement into the following generalized form:

Minimize k , s.t. condition(k) is True

The following code is the most generalized binary search template:

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
   
What's really nice of this template is that, for most of the binary search problems, we only need to modify three parts after copy-pasting this template, and never need to worry about corner cases and bugs in code any more:

Correctly initialize the boundary variables left and right. Only one rule: set up the boundary to include all possible elements;
Decide return value. Is it return left or return left - 1? Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;
Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.


这道题的中心思想：
从零到最大中， 用bs方法随便定义一个distance的值，然后看小于这个值的有多少个，是否符合k个的给定目标，如果符合，那这个定义的distance就是答案了。
找小于distance的count#的时候 不要用两个forloop不停从头到尾双指针
j的指针是while定义的 不停的+1就可以 当i增加的时候 j也不需要从头来过 因为list被排序过了，j以前的肯定小于distance。