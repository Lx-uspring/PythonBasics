# Name:LiuXing
# DateTime:2020/10/11 0011 2:24
# Details:Python输出函数print

# 输出数字
print(1)
print(1.1)

# 输出字符串
print('111')

# 输出运输表达式
print(1+2)

# 将数据输出到文件中,a+表示如果文件不存在就创建,文件存在内容追加
fp=open("D:/test.txt",'a+')
print('Hello File',file=fp)
fp.close()

