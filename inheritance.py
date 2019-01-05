

class BoardCls(object):
    def method1(self): return 'boardClass1'

bc = BoardCls()
print(bc, bc.method1())
print(' ')


class BoardContentsCls(BoardCls):
    def method1(self): return 'boardContentsClass1'
    def method2(self): return 'boardContentsClass2'

bcc = BoardContentsCls()
print(bcc, bcc.method1())
print(bcc.method2())
print(' ')

# bicc method1 존재하지 않는다. 부모에서 method1 찾아 리턴
class BoardInheritanceContentsCls(BoardCls):
    def method2(self): return 'boardInheritanceContentsClass1'

print('상속된 메소드 결과 값 리턴')
bicc = BoardInheritanceContentsCls()
print('클래스의 메소드 결과 값 리턴')
print(bicc, bicc.method1())
print(' ')
