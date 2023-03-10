"""
추상화란?
필요하지 않은 정보는 숨기고 중요한 정보만을 표현하는 것을 말한다.
공통의 속성이나 값, 메서드를 하나로 묶어서 이름을 붙이는 것이다.
"""


class Gpt:

    """
    [Gpt 클래스]
    Author: jake
    Contents: Gpt class
    """

    # 클래스 변수
    population = 0

    # 생성자 함수
    def __init__(self,name, code):
        self.name = name
        self.code = code
        Gpt.population += 1

    # instance methods
    def say_hello(self):
        print(f"Hello!my name is {self.name}")

    def add_calculator(self, a, b):
        print(a + b)
        return a + b

    def say_bye(self):
        print("Bye")

    # class methods
    # 각각의 인스턴스

    # 클래스 변수와 클랜스 메소드는 없을까? 있다!
    @classmethod
    def how_many(cls):
        print(f"we have {cls.population} gpt")

    @staticmethod
    def wow_gpt():
        print('hihi!')


gpt1 = Gpt("gpt1", 3214032)
gpt2 = Gpt("gpt2", 3214032)
gpt3 = Gpt("gpt3", 3214032)

gpt1.say_hello()
gpt2.say_bye()
gpt3.add_calculator(1,3)
Gpt.how_many()

# name_space
print(Gpt.__dict__)  # 클래스에 인스턴스 메소드가 있음.
print(gpt1.__dict__) # 인스턴스는 인스턴스 변수만 있음. 메모리 효율을 위함.

print(gpt1.population) # 인스턴스도 클래스 변수에 접근이 가능하다.

print(Gpt.say_bye(gpt1))

# dir()
# namespace의 키를 확인할 수 있음.
# __doc__ 클래스의 주석을 확인할 수 있음.
# __class__ 어떤 클래스로 만들어지 인스턴스인지 확인 가능.

print(dir(gpt2))

print(dir(Gpt))
print(Gpt.__doc__)
print(Gpt.__class__)

print(gpt1.wow_gpt())