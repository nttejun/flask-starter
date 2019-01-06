import unittest
from inheritance import *

class InheritanceTest(unittest.TestCase):
    def test_boardcls_method1(self):
        result = BoardCls.method1(self)
        self.assertEquals(result, 'boardClass1')

    def test_boardContentsCls_method1(self):
        result = BoardContentsCls.method1(self)
        self.assertEquals(result, 'boardContentsClass1')

    def test_boardContentsCls_method2(self):
        result = BoardContentsCls.method2(self)
        self.assertEquals(result, 'boardContentsClass2')

    # 클래스의 메소드 실행결과를 리턴한다.
    def test_boardInheritanceContentsCls_method1(self):
        result = BoardInheritanceContentsCls.method1(self)
        self.assertEquals(result, 'boardClass1')

    # 상속받은 부모 클래스의 메소드 실행결과를 리턴한다.
    def test_boardInheritanceContentsCls_method2(self):
        result = BoardInheritanceContentsCls.method2(self)
        self.assertEquals(result, 'boardInheritanceContentsClass1')

if __name__ == '__main__':  
    unittest.main()