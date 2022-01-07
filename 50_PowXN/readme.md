这是一道recursion的题 但是用了类似binarysearch的思路
bigO: logN
我一开始想的是 n-1 这样recursion下去但是太耗时间，可以//2 这样减半

recursion base case：
当n=0 的时候注意是 return1 而不是returnx

wrong case:
x=0.00001
n=2147483647
max recursion depth


为什么不能写成： return  self.myPow(a, b // 2) *  self.myPow(a, b // 2)
A：
在每一层的时候你计算了一次self.myPow(a, b // 2)， 然后赋值给了half，你之后调用的不是self.myPow(a, b // 2)这个运算，而是之气前self.myPow(a, b // 2)运算之后得到的值，所以你是对一个值的两次调用，而不是一个运算的两次调用
给你举个例子：

def add_twice(x, y):
    half = x + y  #2
    return half + half

print(add_twice(1, 1))
这个代码里面，你在half的那层计算了一次，half这个时候等于2
所以当你return half + half 的时候，你return的是 2 + 2， 而不是 (1 + 1) + (1 + 1)
懂了么？

然后我还想说的就是，如果你这个细节懂了以后，即使你在面试过程中用的是你之前的代码，也可以跟面试官说，我可以这么这么优化。
记住不要背答案，根基才是面试官考你的点。