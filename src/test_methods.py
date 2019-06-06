import pytest
import unittest
def test_method_A():
    print("Test METHOD A \n")


def test_method_B():
    print("Test METHOD B \n")

def test_method_C():
    print("Test METHOD C \n")

def test_method_D():
    print("Test METHOD D \n")

def test_method_E():
    print("Test METHOD E \n")


class TestMyTest:
    def test_MyTest_A(self):
        print("Inside Class MYTEST AND METHOD A\n")

class TestHomePage(unittest.TestCase):
    def setUp(self):
        print("\nSetup MEthod \n")


    def test_TC001(self):
        print("TC001 \n")

    def test_TC002(self):
        print("TC002 \n")

    def test_TC003(self):
        print("TC003 \n")

    def test_TC004(self):
        print("TC004 \n")

    def tearDown(self):
        print("Tear Down Method \n")