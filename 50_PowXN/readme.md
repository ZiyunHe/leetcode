这是一道recursion的题 但是用了类似binarysearch的思路
bigO: logN
我一开始想的是 n-1 这样recursion下去但是太耗时间，可以//2 这样减半

recursion base case：
当n=0 的时候注意是 return1 而不是returnx

wrong case:
x=0.00001
n=2147483647
max recursion depth