anagram 是回文构词法

Anagram（回文构词法）是指打乱字母顺序从而得到新的单词，比如”dormitory” 打乱字母顺序会变成”dirty room” ，”tea” 会变成”eat”。
回文构词法有一个特点：单词里的字母的种类和数目没有改变，只是改变了字母的排列顺序。
因此，将几个单词按照字母顺序排序后，若它们相等，则它们属于同一组anagrams

7/2/22 想法
这个难道不就是bigo(n) 把两个string都loop一遍 看是否有不一样的字母？用hashset保存一下？
或者用python sort 然后看两个是否相等？

犯了个cornercase错误：
没有先找最短的string，再储存
比如
"ab"
"a"
这时候b已经存在hashet其实应该不相等。

又cornercase错误
重复的字母，用hashset的话 不记录重复。
"aacc"
"ccac"

如何删除map key？
del my_dict[key]
my_dict.pop('key', None)

结果时间30% 空间34%

best soulution是
# 无语子
python有个方法叫counter
>>> word = "mississippi"
>>> counter = {}

>>> for letter in word:
...     if letter not in counter:
...         counter[letter] = 0
...     counter[letter] += 1
...

>>> counter
{'m': 1, 'i': 4, 's': 4, 'p': 2}