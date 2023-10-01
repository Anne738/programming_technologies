import unittest
import prog

class TestOrderStack(unittest.TestCase):
    def setUp(self):
        self.order = prog.OrderStack()
  
    def test_add1(self):
        self.assertEqual(self.order.push("kk", 2), None)

    def test_add2(self):
        self.assertFalse(self.order.push(4,0))
 
    def test_addexept(self):
        with self.assertRaises(TypeError):
            self.order.push()

    def test_pop1(self):
        self.order.push("", 3)
        self.assertEqual(self.order.pop(), -1)

    def test_popexept(self):
        with self.assertRaises(IndexError):
            self.order.pop()

    def test_view(self):
        self.assertEqual(self.order.view(), None)



if __name__ == "__main__":
    unittest.main()
