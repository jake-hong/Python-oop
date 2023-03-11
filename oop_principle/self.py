# self에 대하여
# self는 인스턴스 객체다. 주소 값이 동일하다!


class Self:

    name = "jake"

    def __init__(self, x):
        self.x = x

    @classmethod
    def func1(cls):
        print(f"cls:{cls}")
        print("func1")

    def func2(self):
        print(f"self:{self}")
        print("class안의 self 주소 :",id(self))
        print("func2")


test_obj = Self(17)
test_obj.func2()
test_obj.func1()

print("인스턴스의 주소:", id(test_obj))

'''
self:<__main__.Self object at 0x104b4a0d0>
class안의 self 주소 : 4373913808
func2
cls:<class '__main__.Self'>
func1
인스턴스의 주소: 4373913808
'''