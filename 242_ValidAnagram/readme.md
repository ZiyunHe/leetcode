anagram 是回文构词法

Anagram（回文构词法）是指打乱字母顺序从而得到新的单词，比如”dormitory” 打乱字母顺序会变成”dirty room” ，”tea” 会变成”eat”。
回文构词法有一个特点：单词里的字母的种类和数目没有改变，只是改变了字母的排列顺序。
因此，将几个单词按照字母顺序排序后，若它们相等，则它们属于同一组anagrams

7/2/22 想法
这个难道不就是bigo(n) 把两个string都loop一遍 看是否有不一样的字母？用hashset保存一下？
或者用python sort 然后看两个是否相等？

