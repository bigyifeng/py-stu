class Custom(object):
    def __init__(self):
        print("类的初始化")
        self.a = 1
        self.b = 1

    def __str__(self):
        return "类的print打印显示"

    def __len__(self):
        return 666666

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.b + self.a
        if self.a > 99999:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        return n


c = Custom()
print(c)
print(len(c))


for i in c:
    print(i)

print(c[66666])
