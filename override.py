class C1:
    def m(self):
        return 'parent'
    def m2(self):
        return 'parent2'

class C2(C1):
    # C1(부모) 메서드를 C2(자식)에서 원하는 기능으로 구현한 메서드를 사용할 수 있다.
    def m(self):
        return 'child'
    # super().m2() 입력한 코드는 m2 메서드가 가르키는 C1(부모)의 메소드를 호출한다.
    def m2(self):
        return super().m2() + ' child'
    # pass 메소드가 존재하지 않는 클래스를 사용할 수 있다.
    pass

o = C2()
print(o.m2())