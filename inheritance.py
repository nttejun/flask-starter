class BoardCls(object):
    def method1(self): return 'boardClass1'

class BoardContentsCls(BoardCls):
    def method1(self): return 'boardContentsClass1'
    def method2(self): return 'boardContentsClass2'

class BoardInheritanceContentsCls(BoardCls):
    def method2(self): return 'boardInheritanceContentsClass1'
