import unittest
#import entity.Set as Set
from entity import Set

class SetTest(unittest.TestCase):

    s1 = Set.Set()
    s1.put('mama')
    s1.put('papa')
    s1.put('johnny')
    s1.put('tree')
    s1.put('eye')

    s2 = Set.Set()
    s2.put('papa')
    s2.put('bread')
    s2.put('johnny')
    s2.put('log')

    def test_remove(self):
        set1 = Set.Set()
        set1.put('3')
        set1.put('4a')
        set1.remove('3')
        self.assertEqual({'18.0': '4a'}, set1.storage)

    def test_put(self):
        set = Set.Set()
        set.put('aaa')
        set.put('aaa')
        self.assertEqual({'10.0': 'aaa'}, set.storage)

    def test_intersection(self):

        self.assertEqual(self.s1.intersection(self.s2).storage, {'2.0': 'papa', '11.0': 'johnny'})

    def test_issubset(self):
        s3 = Set.Set()
        s3.put('1')
        s3.put('2')
        s3.put('3')
        s3.put('10')
        s3.put('10001')

        s4 = Set.Set()
        s4.put('3')
        s4.put('10001')

        self.assertTrue(s4.issubset(s3))

    def test_difference(self):
        self.assertEqual(self.s1.difference(self.s2).storage, {'0.0': 'tree', '4.0': 'eye', '7.0': 'mama'})

    def test_union(self):
        self.assertEqual(self.s1.union(self.s2).storage, {'4.0': 'eye', '5.0': 'papa', '11.0': 'johnny', '1.0': 'log', '0.0': 'tree', '7.0': 'mama', '2.0': 'bread'})



if __name__ == '__main__':
    unittest.main()