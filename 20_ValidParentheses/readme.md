7/3/22 想法
 从头到尾过一遍，建立一个map key是char value是数量，遇到就加减。最后检查长度是否为0

python char ascii
>>> ord('a')
97
>>> chr(97)
'a'
>>> chr(ord('a') + 3)
'd'

how to init a set?
set = {'a', 'b', 'c'}

想法遇到corner case:
"([)]"

重新想：用stack

python get last element:
>>> list[-1:] # returns indexed value
    [3]
>>> list[-1]  # returns value
    3

再次遇到corner case:
"]"

结果时间13% 内存69%

