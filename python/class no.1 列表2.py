b = [1, 2, 3]
# index函数,返回值匹配的第一个匹配项的索引，匹配项可能的区间开始位置和结束位置是可选项
print(23, b.index(1))
# 增加列表 列表名.insert(插入点的索引位置（同样0表示第一个），值)
b.insert(3, 4)  # 把4插入到list的第“3”个位置[实际上第4位]
print(b)
# 倒数第n个同样ok，此时会输出[1,2,3,5,4]
b.insert(-1, 5)
print(b)
# 用append可以表示直接插入到最后，但只能插入一个
b.append(6)
print(b)
# 最后插入多个，可以直接使用集合的计算,但b+[7,8,9]并没有改变b的值,同样的可以使用b+=[7,8,9]
print(b + [7, 8, 9])
b = b + [7, 8, 9]
# 用extend可以连接列表，不同于使用“+”，它会直接修改当前列表,extend的参数是列表，它会把列表中各个元素都补充到原列表中
b.extend([10, 11, 12])
# print(b)
# extend与append的区别，append直接把参数作为一个元素插入列表，参数可以是任何类型，包括列表（因为列表的元素可以是列表）但是直接追加，不会像extend一样处理
b.append([13, 14])
print(b)
# print(b - [8, 9])会报错
# 列表复制 list*n等于list+list+list+……
c = [1, 2] * 3
print(c)
# 移除要用pop,参数为索引,为空则默认删除最后一个，pop方法会返回值，返回的值是被删除的元素——可以使用pop实现删除同时把删除的值存储起来。避免误删同时方便回溯
delete_num = b.pop()
print(b)
print(19, delete_num)
print(b)
b.pop(1)
print(b)
b.pop()
print(b)
# del(基于索引)、remove（可基于值）也可以用于删除
del b[2]
print(b)
del b[:2]
print(b)
# remove() 方法只会删除第一个和指定值相同的元素，而且必须保证该元素是存在的，否则会引发 ValueError 错误。
b.remove(8)
print(b)
# 修改直接用索引切片
b[2] = 3
b[1] = 2
print(b)
# clear清空列表
b.clear()
print(b)
# 二维列表
c = [[1, 2], [3, 4]]
print(c)
b = [3, 4]
d = [1, 2]
c = [b, d]
print(c)
# 第一个元素是[3,4],第二个元素是[1,2]
# 二维列表索引
print(c[0])
print(c[0][1])
# 多维列表的快速生成，numpy更直观
e = [b] * 3  # [b]就是一个以列表b为元素的列表
print(e)

# list可以包含任何类型的数据，甚至变量【直接引用值，但值不会跟着变，因为python是给值附上变量的名，变值==给新值附上旧名】
a = 1
b = 2
c = [a, b]
print(c)
a += 1
print(c, a)
# 对比
d = ["a", "b"]  # 有括号是字符串不是变量
print(d)

# list的映射：对list中的每一个元素都应用同一个函数，在映射为另一个list，原list不变
l = [1, 2, 3]
print([elem - 1 for elem in l], l)  # 把list中每一个元素都暂时赋给变量elem（可起任意名，就是中转站），对elem应用函数计算再返回到list中

# 列表的判断
a = [1, 2, 3]
print([1, 2] < a)

# 列表排序函数 list.sort() 参数reverse 默认升序[为false]，为true则降序，直接修改lst,无返回值
p = [1, 3, 4, 2, 6, 7, 9, 1]
p.sort()
print(p)
p.sort(reverse=True)
print(p)
# list.reverse()直接降序排序
p.sort()
p.reverse()
print(p)
# 内置排序函数sorted()它会返回一个新list
p = [1, 3, 4, 2, 6, 7, 9, 1]
print(sorted(p))
print(p.sort())  # list.sort()无返回值
# 打乱顺序 random的shuffle函数
import random
random.shuffle(p)
print(p)

