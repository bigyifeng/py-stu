# 装饰器
def log2(func):
    def wrapper(*args, **kw):
        print(f"call is {func.__name__}")
        return func(*args, **kw)

    return wrapper


# 有参数的装饰器
def log(des):
    def decorator(func):
        def wrapper(*args, **kw):
            print(f"{des}:call is {func.__name__}")
            return func(*args, **kw)

        return wrapper

    return decorator


@log("add的描述")
def add(a, b):
    return a + b


@log("remove的描述")
def remove(a, b):
    return a - b


add(1, 2)
remove(1, 2)


import time, functools

from datetime import datetime

# 获取当前时间戳
current_timestamp = datetime.now().timestamp()


def metric(fn):

    def wrapper(*args, **kw):
        start_time = datetime.now().timestamp()
        res = fn(*args, **kw)
        end_time = datetime.now().timestamp()
        print(f"{fn.__name__}函数执行时间:{(end_time - start_time):.4f}")
        return res

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print("测试失败!")
elif s != 7986:
    print("测试失败!")
