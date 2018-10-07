import unittest
#import entity.Set as Set
from entity import Set

class SetTest(unittest.TestCase):

    def test_remove(self):
        set = Set.Set()
        set.put('3')
        set.put('4a')
        set.remove('3')
        self.assertNotIn({'13.0': '3'}, set.storage)

    if __name__ == '__main__':
        unittest.main()