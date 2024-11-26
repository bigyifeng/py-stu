def normalize(name):
    return name[0].upper() + name[1:].lower()


# 测试:
L1 = ["adam", "LISA", "barT"]
L2 = list(map(normalize, L1))
print(L2)

print("----------------------------------------------------------")

from functools import reduce


def prod(L):
    return reduce(lambda x, y: x * y, L)


print("3 * 5 * 7 * 9 =", prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print("测试成功!")
else:
    print("测试失败!")

print("----------------------------------------------------------")


def str2float(s):
    point_num = s.find(".")
    print(point_num)

    arr1 = s[:point_num]
    arr2 = s[point_num + 1 :]
    print(arr1)
    print(len(arr2))

    return reduce(lambda x, y: int(x) * 10 + int(y), arr1) + reduce(
        lambda x, y: int(x) * 10 + int(y), arr2
    ) / (10 ** len(arr2))


print("str2float('123.456') =", str2float("123.456"))
if abs(str2float("123.456") - 123.456) < 0.00001:
    print("测试成功!")
else:
    print("测试失败!")


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


# 测试:
output = filter(is_palindrome, range(1, 1000))
if list(filter(is_palindrome, range(1, 200))) == [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    11,
    22,
    33,
    44,
    55,
    66,
    77,
    88,
    99,
    101,
    111,
    121,
    131,
    141,
    151,
    161,
    171,
    181,
    191,
]:
    print("测试成功!")
else:
    print("测试失败!")


L = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Lisa", 88)]


def by_score(t):
    return -t[1]


L2 = sorted(L, key=by_score)
print(L2)


L = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Lisa", 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)
