import unittest

# 你的业务类
class Supplement:
    def __init__(self, name, stock, daily_take_in):
        self.name = name
        self.stock = stock 
        self.daily_take_in = daily_take_in

    def take_in(self):
        if self.stock >= self.daily_take_in:
            self.stock -= self.daily_take_in
            return True # 服用成功
        return False # 库存不足

# --- 优雅的测试类 ---
class TestSupplementAdvanced(unittest.TestCase):
    
    def setUp(self):
        """
        这个方法在每个 test_ 函数运行前都会跑一次。
        就像每次实验前，质检员都去仓库领一瓶崭新的、装有 20 粒的 D3。
        """
        # 注意：这里必须用 self. 把药瓶挂在质检员身上
        self.my_d3 = Supplement('d3', 20, 2)
    
    def test_take_in_success(self):
        # 1. 检查动作的“结果”是否为真
        result = self.my_d3.take_in()
        self.assertTrue(result) # 确认返回了 True
    
    def test_single_take_in(self):
        """测试服用一次后库存是否正确"""
        self.my_d3.take_in()
        self.assertEqual(self.my_d3.stock, 18)
        
    def test_multiple_take_in(self):
        """测试服用两次后库存是否正确"""
        self.my_d3.take_in()
        self.my_d3.take_in()
        self.assertEqual(self.my_d3.stock, 11)

if __name__ == '__main__':
    unittest.main(verbosity=2)
