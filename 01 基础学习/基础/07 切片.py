# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

from doctest import debug
from re import L


# 写法1
def trim1(s):
    start = 0
    end = 0
    for i in range(len(s)):
        if s[i] != " ":
            start = i
            break
    for i in range(len(s)):
        if s[-(i + 1)] != " ":
            end = len(s) + (-i)
            break
    return s[start:end]


# 写法2
def trim2(s):
    start = 0
    end = len(s)
    while start < len(s) and s[start] == " ":
        start += 1
    while end > 0 and s[end - 1] == " ":
        end -= 1
    return s[start:end]


# 写法3
def trim(s):
    if len(s) == 0:
        return ""
    if s[0] == " ":
        return trim(s[1:])
    elif s[-1] == " ":
        return trim(s[:-1])
    else:
        return s


# 测试:
if trim("hello  ") != "hello":
    print("测试失败!")
elif trim("  hello") != "hello":
    print("测试失败!")
elif trim("  hello  ") != "hello":
    print("测试失败!")
elif trim("  hello  world  ") != "hello  world":
    print("测试失败!")
elif trim("") != "":
    print("测试失败!")
elif trim("    ") != "":
    print("测试失败!")
else:
    print("测试成功!")
