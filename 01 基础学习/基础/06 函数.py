def add(a, b=6):
    if a > 1:
        pass
    if a > 10:
        print("a > 10")
        a = -1
    return a + b


print(add(2, 2))
print(add(12, 2))


print("===================================================")


# 参数顺序改变
def concat(first, last):
    print(f"顺序: {first} {last}")


concat("first", "last")
concat(last="last", first="first")

print("===================================================")


def person(name, age, **kw):
    if "city" in kw:
        # 有city参数
        pass
    if "job" in kw:
        # 有job参数
        pass
    print("name:", name, "age:", age, "other:", kw)


di = {"age": 24, "ct": "  ct"}

person("Jack", **di)

print("===================================================")

def mul(*args):
    # 如果没有参数传入，则抛出 TypeError 异常
    if len(args) == 0:
        raise TypeError("至少需要一个参数")
    
    # 初始化乘积变量为 1，而非 0
    product = 1
    
    # 遍历所有参数并计算乘积
    for num in args:
        product *= num
        
    return product

# 测试
print("mul(5) =", mul(5))
print("mul(5, 6) =", mul(5, 6))
print("mul(5, 6, 7) =", mul(5, 6, 7))
print("mul(5, 6, 7, 9) =", mul(5, 6, 7, 9))

# 测试空参数调用
try:
    mul()
    print("mul()测试失败!")  # 这一行不应该被执行
except TypeError:
    print("测试成功!")  # 正确捕获了异常，测试成功