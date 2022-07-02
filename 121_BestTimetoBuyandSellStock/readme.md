7/2/22 想法
 从头到尾loop一遍 bigo(n)
 三个placeholder， min，max，diff
 第一个点算低点，然后持续找最高点高点，找到以后算差值，保存最大差值。
 如果遇到新的低点，reset高点为0
leetcode结果时间67.41%，内存38.00%

best solution
不用三个值，只用最小和 最大差值
如果遇到更低的小的 就是更新
然后继续loop的时候就算差值，如果更大了就记录。
