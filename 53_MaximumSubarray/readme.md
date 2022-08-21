7/3/22 想法
  两个指针 头和尾，算头尾之间的sum（包括头尾）。每次往里缩短指针，重新算sum。保存最大
  如果减去左边的大，就缩短左指针，如果右边大，就缩短右指针
  big o of N

python get list sum:
list1 = [11, 5, 17, 18, 23]
total = sum(list1)

想法不对 如果是4,-1,2,1,-5,4情况，去掉哪边？
一半一半大算，左边少还是右边少

corner case:
[-2,-1]

8/20 想法
用一个hash 保存有所值，用index为key
然后recursion循环，以两个为单位，直到达到arry长度

答案：
动归：
f[i] = 指包括 nums[i] 在内的maximum sum subarray
----------
The meaning of f(i): the maximum sum subarray including nums[i]
The key point is HAVE TO including nums[i]
----------
f[i] = maxSubArray(0..i)
f[i] = f[i-1] > 0 ? nums[i] + f[i-1]: nums[i]
