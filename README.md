# leetcode

从零开始leetcode

参考资源：\
花花酱题目列表： https://docs.google.com/spreadsheets/d/1yRCOJ8KysRVkq0O9IlDriT01tC6lzPapmFO4PCmDJQA/edit?usp=sharing \
九章算法题目列表： https://drive.google.com/file/d/12oo68w4AafEGyvQZ1BA7Xgb6auITUQjP/view?usp=sharing \
代码随想录刷题攻略： https://github.com/youngyangyang04/leetcode-master \
图灵栖息地刷题表 https://turingplanet.org/2020/09/18/leetcode_planning_list/ \
LeetCode难题代码和算法要点分析w/ youtube video:  https://github.com/wisdompeak/LeetCode \
Blind75: https://www.techinterviewhandbook.org/best-practice-questions/

做题方式：
1. 5分钟读懂题 + 想思路，如果完全没有想法就看答案吧
2. 想出各种cases
3. 检查思路是否适用
4. 白板写代码
5. 跑的时候bugfree

每题时间：\
1 个半小时 4 道题： 1 简单，2 中等，1 困难\
大概easy 10, medium20, hard30

生成做题/复习计划表格：https://exam4.us/

题目：(Jan/2/21 update)

**Binary Search 二分搜索**

花花酱：\
Id	Name	Similar Difficulty	Comments\
35.Search Insert Position	\
   34 704	981	★★ upper_bound\
33.Search in Rotated Sorted Array\
   81	153	154	162	852 ★★★	rotated / peak\
69.Sqrt(x)\
   ★★★	upper_bound\
74.Search a 2D Matrix\
   ★★★	treat 2d as 1d\
875.Koko Eating Bananas\
   1011 ★★★ guess ans and check\
4.Median of Two Sorted Arrays\
   ★★★★								\
378.Kth Smallest Element in a Sorted Matrix\
   668 ★★★★	kth + matrix\
719.Find K-th Smallest Pair Distance\
   786 ★★★★	kth + two pointers
   
九章(lintcode):\
★\
457.Classical Binary Search\
14.First Position of Target\
458.Last Position of Target\
★★\
585.Maximum Number in Mountain Sequence\
460.Find K Closest Elements\
447.Search in a Big Sorted Array\
159.Find Minimum in Rotated Sorted Array 140.Fast Power\
140.Fast Power\
50.Pow(x, n)\
75.Find Peak Element\
74.First Bad Version\
62.Search in Rotated Sorted Array\
★★★\
28.Search a 2D Matrix\
38.Search a 2D Matrix II\
61.Search for a Range\
462.Total Occurrence of Target\
600.Smallest Rectangle Enclosing Black Pixels\
437.Copy Books


**Two Pointers 双指针**

花花酱：\
11.Container With Most Water\
   42 ★★							\
125.Valid Palindrome\
   455 ★★							\
917.Reverse Only Letters\
   925	986	855 ★★\
977.Squares of a Sorted Array				\				
   ★★ merge sort\
167.Two Sum II – Input array is sorted\
   15	16 ★★★						\
992.Subarrays with K Different Integers\
   ★★★★								

九章:\
★\
228.Middle of Linked List\
607.Two Sum III - Data structure design\
539.Move Zeroes\
521.Remove Duplicate Numbers in Array\
464.Sort Integers II\
★★\
608.Two Sum II - Input array is sorted\
143.Sort Colors II\
57.3Sum\
31.Partition Array\
5.Kth Largest Element\
604.Window Sum\
380.Intersection of Two Linked Lists\
102.Linked List Cycle\
103.Linked List Cycle II\
380.Intersection of Two Linked Lists\
415.Valid Palindrome\
891.Valid Palindrome II\
587.Two Sum - Unique pairs\
382.Triangle Count\
609.Two Sum - Less than or equal to target\
443.Two Sum - Greater than target\
★★★\
533.Two Sum - Closest to target\
59.3Sum Closest\
58.4Sum\
610.Two Sum - Difference equals to target\
461.Kth Smallest Numbers in Unsorted Array\
373.Partition Array by Odd and Even\
144.Interleaving Positive and Negative Numbers\
49.Sort Letters by Case\
148.Sort Colors\
894.Pancake Sorting


**BFS & Topological Sort & DFS 宽度/深度优先搜索**

花花酱：\
17	Letter Combinations of a Phone Number	★★	39	40	77	78	90	216		\
Combination\
46	Permutations	★★	47	784	943	996				Permutation\
22	Generate Parentheses	★★★	301							DFS\
37	Sudoku Solver	★★★	51	52						DFS\
79	Word Search	★★★	212							DFS\
127	Word Ladder	★★★★	126	752	818					BFS\
542	01 Matrix	★★★	675	934						BFS\
698	Partition to K Equal Sum Subsets	★★★	93	131	241	282	842	Partition

九章：\
BFS:\
★\
433.Number of Islands\
69.Binary Tree Level Order Traversal\
★★\
70.Binary Tree Level Order Traversal II\
615.Course Schedule\
616.Course Schedule II\
611.Knight Shortest Path\
605.Sequence Reconstruction\
137.Clone Graph\
127.Topological Sorting\
120.Word Ladder\
7.Serialize and Deserialize Binary Tree\
71.Binary Tree Zigzag Level Order Traversal\
242.Convert Binary Tree to Linked Lists by Depth\
★★★\
892.Alien Dictionary\
178.Graph Valid Tree\
618.Search Graph Nodes\
431.Connected Component in Undirected Graph\
598.Zombie in Matrix\
573.Build Post Office II\
DFS:\
★\
680.Split String\
★★\
570.Find the Missing Number II\
136.Palindrome Partitioning\
153.Combination Sum II\
152.Combinations\
135.Combination Sum\
18.Subsets II\
17.Subsets\
★★★\
780.Remove Invalid Parentheses\
582.Word Break II\
192.Wildcard Matching\
154.Regular Expression Matching\
90.k Sum II


**Binary Tree & Tree-based DFS & BST 二叉搜索树**

花花酱：\
98.Validate Binary Search Tree\
   530 ★★	inorder\
700.Search in a Binary Search Tree\
   701 ★★ binary search\
230.Kth Smallest Element in a BST\
   ★★★						inorder\
99.Recover Binary Search Tree\
   ★★★ inorder\
108.Convert Sorted Array to Binary Search Tree\
   ★★★ build BST\
501.Find Mode in Binary Search Tree\
   ★★★ inorder\
450.Delete Node in a BST\
   ★★★★	binary search

九章：\
★\
900.Closest Binary Search Tree Value\
596.Minimum Subtree\
480.Binary Tree Paths\
453.Flatten Binary Tree to Linked List\
93.Balanced Binary Tree\
★★\
902.Kth Smallest Element in a BST\
578.Lowest Common Ancestor III\
95.Validate Binary Search Tree\
★★★\
901. Closest Binary Search Tree Value II\
86.Binary Search Tree Iterator\
597.Subtree with Maximum Average\
175.Invert Binary Tree\
95.Validate Binary Search Tree\
596.Minimum Subtree\
88.Lowest Common Ancestor of a Binary Tree\
86.Binary Search Tree Iterator\
448.Inorder Successor in BST\
67.Binary Tree Inorder Traversal\
11.Search Range in Binary Search Tree\
85.Insert Node in a Binary Search Tree\
87.Remove Node in Binary Search Tree 


**Tree 树**

花花酱：\
94.Binary Tree Inorder Traversal\
   144	145	429	589	590 987	1302 ★	traversal\
100.Same Tree\
   101	104	110	111	572 965	 ★★ \
102.Binary Tree Level Order Traversal\
   107	429	872 ★★	collecting nodes\
814.Binary Tree Pruning\
   669 1325 ★★★ \
112.Path Sum\
   113 437 ★★★	\
129.Sum Root to Leaf Numbers \
   257 ★★★ \
236.Lowest Common Ancestor of a Binary Tree\
   235 ★★★ \
297.Serialize and Deserialize Binary Tree\
   449 ★★★ \
508.Most Frequent Subtree Sum\
   ★★★\
124.Binary Tree Maximum Path Sum\
   543	687 ★★★	Use both children, return one\
968.Binary Tree Cameras\
   337	979	★★★★


**Divide and Conquer 分治**

花花酱：\
169.Majority Element\
    ★★	你知道茴香豆的茴有几种写法吗？\
153.Find Minimum in Rotated Sorted Array\
    ★★	154\
912.Sort and Array\
    ★★★	merge sort\
315.Count of Smaller Numbers After Self\
    ★★★★	merge sort / BIT


**List 链表**

花花酱：\
2.Add Two Numbers\
  445 ★★	traversal\
24.Swap Nodes in Pairs\
  ★★ reverse\
206.Reverse Linked List\
  ★★ reverse\
141.Linked List Cycle\
  142 ★★	fast/slow\
23.Merge k Sorted Lists\
  21 ★★★	priority_queue / mergesort\
147.Insertion Sort List\
  ★★★	insertion sort\
148.Sort List\
  ★★★★	merge sort O(1) space\
707.Design Linked List\
  ★★★★
  

**Graph & permutation-based+graph-based DS\F 图 & 排列/图的dfs**

花花酱：\
133.Clone Graph\
   138 ★★	 queue + hashtable\
200.Number of Islands\
   547	695	733	827	1162 ★★	grid + connected components\
841.Keys and Rooms\
   1202	★★	DFS, connected components\
207.Course Schedule\
   210	802 ★★★	topology sorting\
399.Evaluate Division\
   839	952	990	721	737 ★★★	union find\
785.Is Graph Bipartite?\
   886	1042	★★★ bipartition, graph coloring\
997.Find the Town Judge	\
   ★★★	in/out degrees\
433.Minimum Genetic Mutation\
   815	863	1129	1263 ★★★	unweighted shortest path / BFS\
684.Redundant Connection\
   685	1319 ★★★★	cycle, union find\
743.Network Delay Time\
   787	882	924	1334 ★★★★		weighted shortest path\
847.Shortest Path Visiting All Nodes\
   864	1298 ★★★★	BFS\
332.Reconstruct Itinerary\
   ★★★★	Eulerian path\
1192.Critical Connections in a Network\
   ★★★★	Tarjan\
943.Find the Shortest Superstring\
   980	996 ★★★★★	Hamiltonian path (DFS / DP)\
959.Regions Cut By Slashes\
   ★★★★★	union find / grid + CCs

九章\
★★\
862.Next Closest Time\
425.Letter Combinations of a Phone Number\
10.String Permutation II\
34.N-Queens II\
33.N-Queens\
16.Permutations II\
15.Permutations\
★★★\
829.Word Pattern II\
132.Word Search II\
121.Word Ladder II\
33.N-Queens\
52.Next Permutation\
190.Next Permutation II\
197.Permutation Index\
198.Permutation Index II\
132.Word Search II


**Stack,Queue,Hash,Heap**

九章：\
★\
642.Moving Average from Data Stream\
494.Implement Stack by Two Queues\
209.First Unique Character in a String\
★★\
657.Insert Delete GetRandom O(1)\
612.K Closest Points\
544.Top k Largest Numbers\
104.Merge K Sorted Lists\
40.Implement Queue by Two Stacks\
4.Ugly Number II\
★★★\
134.LRU Cache\
526.Load Balancer\
954.Insert Delete GetRandom O(1) - Duplicates allowed 960.First Unique Number in a Stream II\
138.Subarray Sum\
105.Copy List with Random Pointer\
171.Anagrams\
124.Longest Consecutive Sequence\
685.First Unique Number In Stream\
545.Top k Largest Numbers II\
228.Middle of Linked List\
81.Find Median from Data Stream\
613.High Five\
486.Merge K Sorted Arrays\
401.Kth Smallest Number in Sorted Matrix


**Interval, array, matrix, binary indexed tree**

九章：\
★\
839.Merge Two Sorted Interval Lists\
547.Intersection of Two Arrays\
138.Subarray Sum\
64.Merge Sorted Array\
41.Maximum Subarray\
★★\
944.Maximum Submatrix\
931.Median of K Sorted Arrays \
840.Range Sum Query - Mutable \
654.Sparse Matrix Multiplication \
577.Merge K Sorted Interval Lists \
486.Merge K Sorted Arrays\
★★★\
65.Median of two Sorted Arrays\
6.Merge Two Sorted Arrays \
486.Merge K Sorted Arrays \
548.Intersection of Two Arrays II \
793.Intersection of Arrays\
149.Best Time to Buy and Sell Stock \
405.Submatrix Sum\
943.Range Sum Query - Immutable \
665.Range Sum Query 2D - Immutable \
817.Range Sum Query 2D - Mutable \
249.Count of Smaller Number before itself


**Advanced** 

花花酱：\
208.Implement Trie (Prefix Tree)\
   648	676	677	720	745	211 ★★★	Trie\
307.Range Sum Query – Mutable\
   ★★★	BIT/Segment Tree\
901.Online Stock Span\
   907	1019 ★★★	monotonic stack\
239.Sliding Window Maximum\
   ★★★	monotonic queue


**DP**

花花酱：\
70.Climbing Stairs\
   746	1137 ★ I: O(n), S = O(n), T = O(n)\
303.Range Sum Query – Immutable\
   1218 ★				\
53.Maximum Subarray\
   121 ★★					\
62.Unique Paths\
   63	64	120	174	931 1210 ★★	I: O(mn), S = O(mn), T = O(mn)				\
85.Maximal Rectangle\
   221	304	1277 ★★★		\
198.House Robber\
   213	309	740	790	801 ★★★	I: O(n), S = O(3n), T = O(3n)\
279.Perfect Squares\
   ★★★	I: n, S = O(n), T = O(n x sqrt(n))\
139.Word Break\
   140	818	 ★★★	I: O(n), S = O(n), T = O(n^2)\
300.Longest Increasing Subsequence\
   673	1048 ★★★			\
96.Unique Binary Search Trees\
   ★★★					\
1105.Filling Bookcase Shelves\
   ★★★	I: O(n) + t, S = O(n), T = O(n^2)\
131.Palindrome Partitioning\
   89 ★★★	I: O(n), S = O(2^n), T = O(2^n)\
72.Edit Distance\
   10	44	97	115	583 712	1187	1143	1092	718  ★★★	I: O(m+n), S = O(mn), T = O(mn)\
1139.Largest 1-Bordered Square\
   ★★★	I: O(mn), S = O(mn), T = O(mn x min(n,m))\
688.Knight Probability in Chessboard\
   576	935 ★★★	I: O(mn) + k S = O(kmn), T = O(kmn)\
322.Coin Change\
   377	416	494	1043	1049 1220	1230	1262	1269 ★★★	I: O(n) + k, S = O(n), T = O(kn)\
813.Largest Sum of Averages\
   1278	1335	410 ★★★★	I: O(n) + k, S = O(n x k), T = O(kn^2)\
1223.Dice Roll Simulation\
   ★★★★		I: O(n) + k + p, S = O(k x p), T = O(n^2kp)\
312.Burst Balloons\
   664	1024	1039	1140	1130 ★★★★	I: O(n), S = O(n^2), T = O(n^3)\
741.Cherry Pickup\
   ★★★★		I: O(n^2), S = O(n^3), T = O(n^3)\
546.Remove Boxes\
   ★★★★★	I: O(n), S = O(n^3), T = O(n^4)\
943.Find the Shortest Superstring\
   980	996	1125 ★★★★★	I: O(n), S = O(n*2^n), T = (n^2*2^n)

九章\
★\
115.Unique Paths II\
114.Unique Paths\
111.Climbing Stairs\
110.Minimum Path Sum\
109.Triangle\
★★\
603.Largest Divisible Subset \
611.Knight Shortest Path\
513.Perfect Squares\
116.Jump Game\
76.Longest Increasing Subsequence
