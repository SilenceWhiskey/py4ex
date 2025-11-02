# hello world program in my python learning
from base64 import encode

print('hello python')
# print()方法会依次打印每个字符串,遇到英文逗号,会输出一个空格
print('hello', 'world')
# print()方法也可以打印整数或者计算结果
print(1096)
print('100+200 = ', 100 + 200)

# 输入
print('请在控制台输入字符串或数字,输入完成后单击回车键完成')
a = input()
print('你刚刚输入了:', a)

# python中的变量
# None是python中的保留字,表示空值,不能被理解为0,因为0是有意义的,none是一个特殊的空值
# 通常用全大写表示常量
PI = 3.1415926
# /表示除法,//表示整除,%表示取余
# ord()和chr()方法互为逆向效果
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print('字符 李 的ord编码表示为:', ord('李'), '而26445的chr编码表示为:', chr(26445))
# encode()和decode()方法,参数errors = 'ignore'可以忽略错误的字节,len()方法计算str类型数据的字符数(长度),或bytes类型数据的字节数(大小)
# 在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
# 格式化输出,方式和C语言一致!使用%实现或使用format()实现用传入的参数依次替换字符串内的占位符{0}
b = 10
c = 5.5
d = '可乐'
e = 9
f = 4.5
g = '雪碧'
print('我给你{0}元购买价格为{1}元的商品{2}'.format(e, f, g))
print('我给你{0}元购买价格为{1}元的商品{2}'.format(b, c, d))
# f-string是以f' 开头，字符串内的{}直接填写对应的变量名称
s1 = '北京'
s2 = '西安'
print(f'我目前在{s1}学习，以后打算去{s2}就业')
