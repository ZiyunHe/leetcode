7/22/22 想法：
 从头到尾过一遍，用一个map储存。
 map存的 key是target减去当前值，value是当前值的index
 如果loop遇到和mapkey一样的数字，证明这就是答案，直接返回value里的index和当前值的index
 时间是 o(n)
 结果快速50.68%，空间91%

看了最佳答案，我的答案之所以慢是因为用了ifelse，没必要用了因为可以直接return 
