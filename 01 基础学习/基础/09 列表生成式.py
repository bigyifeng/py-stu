import os


l = list(range(2, 10))
print(l)

l1 = [x * x for x in range(2, 5)]
print(l1)

l2 = [print(f"输出：{x}") for x in range(1, 10) if x > 5 and x < 8]

l3 = [x + y + z for x in "ABC" for y in "abc" for z in "123" if y != "b"]
print(l3)


l_dir = [d for d in os.listdir("../")]
print(l_dir)

L1 = ["Hello", "World", 18, "Apple", None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ["hello", "world", "apple"]:
    print("测试通过!")
else:
    print("测试失败!")
