import pytest

#from test_pytest.core.calc import Calc

from test_pytest.core.calc import Calc

## 乘法的测试用例
class TestCalc1:

    def setup_class(self):
        self.calc = Calc()

    #正常值输入：输入为int的情况
    @pytest.mark.parametrize("a, b, c",[
        [1, 2, 2],
        [1, 0, 0],
        [1, -2, -2],
        [-1, -2, 2],
        [100000000, 200000000, 20000000000000000],
        [-100000000, 200000000, -20000000000000000]
    ])
    def test_mul1(self, a, b, c):
        assert self.calc.mul(a, b) == c

    #正常值输入：输入为float的情况
    @pytest.mark.parametrize("a, b, c", [
        [0.1, 0.2, 0.02],
        [0.1, 0.0, 0],
        [0.1, -0.2, -0.2],
        [-0.1, -0.2, 0.02],
        [0.00000001, 0.00000002, 0.0000000000000002],
        [0.00000001, -0.00000002, -0.0000000000000002]
    ])
    def test_mul2(self, a, b, c):
        assert self.calc.mul(a, b) == c

    #正常值输入：输入为int/float的情况
    @pytest.mark.parametrize("a, b, c", [
        [1, 0.2, 0.2],
        [-1, 0.2, -0.2]
    ])
    def test_mul3(self, a, b, c):
        assert self.calc.mul(a, b) == c

    #异常值输入：输入为字符串的情况
    @pytest.mark.parametrize("a, b", [
        ['a', 1],
        ['a', 0.1],
        ['a', 'b'],
        ['a', '#！']
    ])
    def test_mul4(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.mul(a, b)


## 除法的测试用例
class TestCalc2:

    def setup_class(self):
        self.calc = Calc()

    #正常值输入：输入为int的情况
    @pytest.mark.parametrize("a, b, c",[
        [4, 2, 2],
        [-1, 2, -0.5],
        [1, -3 , -0.33333333333333333],
        [5, 3, 1.6666666666666667],
        [-6, -2, 3],
        [0, 1, 0]
    ])
    def test_div1(self, a, b, c):
        assert self.calc.div(a, b) == c

    #正常值输入：输入为float的情况
    @pytest.mark.parametrize("a, b, c", [
        [0.1, 0.2, 0.5],
        [0.1, -0.3, -0.33333333333333333],
        [-0.5, -0.3, 1.6666666666666667],
        [0, 0.2, 0]
    ])
    def test_div2(self, a, b, c):
        assert self.calc.div(a, b) == c

    #正常值输入：输入为int/float的情况
    @pytest.mark.parametrize("a, b, c", [
        [1, 0.2, 5],
        [-0.1, 2, -0.05]
    ])
    def test_div3(self, a, b, c):
        assert self.calc.div(a, b) == c

    #异常值输入：输入为字符串/除数为0的情况
    @pytest.mark.parametrize("a, b", [
        [1, 0],
        [1, 'a'],
        ['a', 1],
        ['a', 0.1],
        ['a', 'b'],
        ['a', '#！']
    ])
    def test_div4(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)


## 流程实例
class TestCalc3:

    def setup_class(self):
        self.calc = Calc()

    #先乘法后除法
    def test_process1(self):
        assert self.calc.mul(1, 2) == 2
        assert self.calc.div(1, 2) == 0.5

    #先除法后乘法
    def test_process2(self):
        assert self.calc.div(1, 2) == 0.5
        assert self.calc.mul(1, 2) == 2