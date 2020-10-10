# Name:LiuXing
# DateTime:2020/10/11 0011 3:25
# Details:

# 赋值打印值
name='LiuXing'
print(name)
# 打印变量标识,多次赋值之后变量名会指向新的内存空间，旧内存变成内存垃圾
print(id(name))
name='LiuXing1'
print(id(name))
# 打印变量类型
print(type(name))


