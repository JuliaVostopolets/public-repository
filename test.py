import pytest
from app.calc import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_sucsess(self):
        assert self.calc.adding(self, 1,1)==2
    def test_adding_unsucsess(self):
      assert self.calc.adding(self,1,2)==4
    def test_substruction(self):
        assert self.calc.subtraction(self,3,2)==1
    def test_multiply(self):
        assert self.calc.multiply(self,4,10)==40
    def test_devision(self):
        assert self.calc.division(self,6,3)==2
    def test_zero_devision(self):
      with pytest.raises(ZeroDivisionError):
          self.calc.division(self,1,0)
    def teardown(sel):
      print('Выплнение метода Teardown')


