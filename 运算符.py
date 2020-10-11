# Name:LiuXing
# DateTime:2020/10/11 0011 11:05
# Details:

# 算数运算 +、-、*、/、//、%、**      注意事项：一正一负整除向下取整
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)

# 赋值运算  顺序从右到左

a=10+1


# 三个变量的标识指向同一个内存空间,当变量的值发生变化时标识会改变
b=c=d=11
print(b,id(b),c,id(c),d,id(d))
d=10
print(b,id(b),c,id(c),d,id(d))

d+=1;
print(d,id(d))

# 解包赋值
e,f,g=1,2,3
print(e,f,g)
# 交换赋值
e,f,g=g,e,f
print(e,f,g)

# 比较运算符
# value比较
print(e>=f)
print(e!=f)
print(e==f)
d=10
# id比较
print(b is d)
print(b is not c)

# 布尔运算符：and or not in not in

print(True and True)
print(False or True)
print(not False)

print(1 in (11,2))
str='Hello'
print('H' in str)
print('Ho' not in str)






