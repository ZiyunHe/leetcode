7/2/22
想法：
 1. 直接一个反手sort，然后顺着loop找不行吗？ bigo是nlogn因为pythonsort是nlogn -> 结果leetcode用时73.85 空间30
 2. 或者建立一个map，如果map里面有值就return true

best solution 用的是第二个想法，但是用的不是map 而是用hashset就可以了

Python hashset:
hashset = set()
hashset.add(xxx)