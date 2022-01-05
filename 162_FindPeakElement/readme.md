1-5-21
每次split的时候该往左走还是右走？难道用recursion？
于是果断放弃想看看了解答 https://www.youtube.com/watch?v=etuTPmks7Dc  太神了
不在乎array排序大小。只有两种情况 升/降

没想到的case：
边缘处也是peak

wrong case: [1,2]

python array没有m - 1 outofbound的时候！！因为nums[-1]是最后一位。。！
只有m+1会out


