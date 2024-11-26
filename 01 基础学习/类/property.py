class Yf:
    def __init__(self):
        self._age = 6
        self.age = 8

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("age must be an integer!")
        elif value < 0 or value > 120:
            raise ValueError("age must between 0~120")
        else:
            self._age = value


yf = Yf()
try:
    print(yf.age)
    yf.age = 200
    print(yf.age)
except AttributeError as e:
    print(e)
except ValueError as e:
    print("属性设置错误", e)
finally:
    print("end")


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, w):
        self._height = w

    @property
    def resolution(self):
        return self.width * self.height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print("resolution =", s.resolution)
if s.resolution == 786432:
    print("测试通过!")
else:
    print("测试失败!")
