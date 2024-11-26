class Student2:
    def __init__(self, name, score):
        self.name = name
        self.score = score


s1 = Student2("Bob", 59)
s2 = Student2("Bob", 59)

print(s1 == s2)
print({"name": "zs"} == {"name": "zs"})


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
bart = Student("Bart", "male")
if bart.get_gender() != "male":
    print("测试失败!")
else:
    bart.set_gender("female")
    if bart.get_gender() != "female":
        print("测试失败!")
    else:
        print("测试成功!")
