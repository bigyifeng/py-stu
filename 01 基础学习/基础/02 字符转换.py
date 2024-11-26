# 字符相互转换
num1 = ord("a")
num2 = ord("糙")
str1 = chr(num1)
str2 = chr(num2)
print(num1)
print(num2)
print(str1)
print(str2)

# encode
code1 = 'YIFENG'.encode('ascii')
code2 = 'YIFENG'.encode('utf-8')
# 不能将中文转为ascii码，会报错
# code3 = '笑死'.encode('ascii')
code4 = '笑死'.encode('utf-8')
print(code1)
print(code2)
print(code4)
print(code1.decode())
print(code2.decode())
print(code4.decode())

# 可以忽略错误
print(b'\xe7\xac\x91\xe6\xaa'.decode('utf-8',errors='ignore'))

print(len(b'YIFENG'),len('YIFENG'),len("靠"),len("靠".encode('utf-8')))


print('%d-%02d' % (3, 1))
print('%.2f' % 3.1415926)


# 小明72到65
s1 = 72 
s2 = 85
print(f"小明成绩提升了{(s2-s1)/s1*100:.2f}%")