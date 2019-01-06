class BoardCls(object):
    def method1(self): return 'boardClass1'

class BoardContentsCls(BoardCls):
    def method1(self): return 'boardContentsClass1'
    def method2(self): return 'boardContentsClass2'

# bicc method1 존재하지 않는다. 부모에서 method1 찾아 리턴
class BoardInheritanceContentsCls(BoardCls):
    def method2(self): return 'boardInheritanceContentsClass1'
