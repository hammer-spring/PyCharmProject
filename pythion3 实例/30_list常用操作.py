print("1.list 定义")
li = ["a", "b", "mpilgrim", "z", "example"]
print(li[1])

print("2.list 负数索引")
print(li[-1])
print(li[-3])
print(li[1:3])
print(li[1:-1])
print(li[0:3])

print("3.list 增加元素")
li.append("new")
print(li)
li.insert(2,"new")
print(li)
li.extend(["two","elements"])
print(li)

print("4.list 搜索")
a = li.index("new")
print(a)
print("c" in li)

print("5.list 删除元素")
li.remove("z")
print(li)
li.remove("new")    # 删除首次出现的一个值
print(li)
#li.remove("c")     #list 中没有找到值, Python 会引发一个异常
#print(li)
print(li.pop())  # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
print(li)

print("6.list 运算符")
li = ['a', 'b', 'mpilgrim']
li = li + ['example', 'new']
print(li)
li += ['two']
print(li)
li = [1, 2] * 3
print(li)

print("8.list 分割字符串")
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print(s)
print(s.split(";") )
print(s.split(";", 1) )

print("9.list 的映射解析")
li = [1, 9, 8, 4]
print([elem*2 for elem in li])
li = [elem*2 for elem in li]
print(li)

print("10.dictionary中的解析")
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
print(params.values())
print(params.items())
print([k for k, v in params.items()])
print([v for k, v in params.items()])
print(["%s=%s" % (k, v) for k, v in params.items()])

print("11.list 过滤")
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print([elem for elem in li if len(elem) > 1])
print([elem for elem in li if elem != "b"])
print([elem for elem in li if li.count(elem) == 1])