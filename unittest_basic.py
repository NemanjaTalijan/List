from elemList import ElemList
from list import List
import unittest

class TestMyFunctions(unittest.TestCase):

    def setUp(self):
        self.elem = ElemList(1)
        self.elem2 = ElemList(2)
        self.newList = List()
        self.pick = ['\n',0,1,100]

    def test_addFront_empty(self):
        self.assertRaises(TypeError,lambda :self.newList.addFront,())

    def test_addFront(self):
        self.assertEqual(self.newList.addFront(self.elem),self.elem)

    def test_addBack(self):
         self.newList.addFront(self.elem)
         self.assertEqual(self.newList.addBack(self.elem),self.elem)

    def test_addBack_empty(self):
        self.assertRaises(TypeError,lambda :self.newList.addBack,())

    def test_pbyi_empty(self):
        self.assertEqual(self.newList.pickbyindex(self.pick),None)

    def test_pbyi_index_not_in_range(self):
        self.newList.addFront(self.elem)
        self.assertEqual(self.newList.pickbyindex(self.pick[1]),self.pick[1])

    def test_pbyi_index_none(self):
        self.newList.addFront(self.elem)
        self.assertEqual(self.newList.pickbyindex(self.pick[0]),self.pick[0])

    def test_pbyi_index_valid(self):
        self.newList.addFront(self.elem)
        self.assertEqual(self.newList.pickbyindex(self.pick[2]),self.pick[2])

    def test_pbyi_index_not_in_rande_upper(self):
        self.newList.addFront(self.elem)
        self.assertEqual(self.newList.pickbyindex(self.pick[3]),self.pick[3])

    def test_revers_empty(self):
        self.assertEqual(self.newList.revers(),None)

    def test_revers_for_two(self):
        self.newList.addFront(self.elem)
        self.newList.addFront(self.elem2)
        self.assertEqual(self.newList.revers(),self.elem)

    def test_printList_empty(self):
        self.assertRaises(TypeError, lambda: self.newList.printList, ())

if __name__ == '__main__':
    unittest.main(exit=False)