import unittest
from fib import fib

class TestFibonacci(unittest.TestCase):
    # 测试样例 1: 基本案例
    def test_base_cases(self):
        self.assertEqual(fib(0), 1, "fib(0) 应该返回 1")
        self.assertEqual(fib(1), 1, "fib(1) 应该返回 1")
    
    # 测试样例 2: 递归案例
    def test_recursive_cases(self):
        self.assertEqual(fib(2), 2, "fib(2) 应该返回 2")
        self.assertEqual(fib(3), 3, "fib(3) 应该返回 3")
        self.assertEqual(fib(4), 5, "fib(4) 应该返回 5")
        self.assertEqual(fib(5), 8, "fib(5) 应该返回 8")

    # 测试样例 3: 较大输入
    def test_large_input(self):
        self.assertEqual(fib(6), 13, "fib(6) 应该返回 13")
        self.assertEqual(fib(7), 21, "fib(7) 应该返回 21")
    
    # 测试样例 4: 无效输入
    def test_invalid_input(self):
        with self.assertRaises(ValueError, msg="负数应该抛出 ValueError"):
            fib(-1)
        with self.assertRaises(ValueError, msg="负数应该抛出 ValueError"):
            fib(-5)
    
    # 测试样例 5: 边界条件
    def test_boundary_condition(self):
        self.assertEqual(fib(10), 89, "fib(10) 应该返回 89")
        self.assertEqual(fib(11), 144, "fib(11) 应该返回 144")

if __name__ == "__main__":
    unittest.main()