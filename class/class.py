# class의 기본 방식

class Cal:

    # 생성자 - 메모리에 올라오면 바로 실행 된다.
    # self - 인스턴스를 지칭한다. 여기서는 아래 cal1, cal2 가 인스턴스.
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


cal1 = Cal(1, 2)
cal2 = Cal(5, 10)

print(cal1.a)
print(cal1.b)
print(cal1.add())

print(cal2.a)
print(cal2.b)
print(cal2.mul())

cal1.a = 3

print(cal1.a)