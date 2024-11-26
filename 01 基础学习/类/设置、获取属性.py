class Student2:
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.x


stu1 = Student2(666)
print(hasattr(stu1, "__x"))
print(hasattr(stu1, "get_x"))

fn = stu1.get_x
fn2 = getattr(stu1, "get_x")
stu1.x = 888

print(fn())
print(fn2())


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print("测试失败!")
else:
    bart = Student("Bart")
    if Student.count != 1:
        print("测试失败!")
    else:
        lisa = Student("Bart")
        if Student.count != 2:
            print("测试失败!")
        else:
            print("Students:", Student.count)
            print("测试通过!")
