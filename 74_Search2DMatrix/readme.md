wrong case:
[[1], [3]]

下一步！：搞懂s, e的加减,  不用ifstate，直接s就等于确定的array 然后往里走
like this:
while l < r:
    mid = (l+r+1)//2
    if matrix[mid][0] > target:
        r = mid - 1
    else:
        l = mid