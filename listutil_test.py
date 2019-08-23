import unittest
from listutil import unique
 
class ListUtilTest(unittest.TestCase):
 
    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )
        self.assertListEqual( [1], unique([1]))
        self.assertListEqual([''], unique(['']))
    
    def test_empty_list(self):
        self.assertListEqual([], unique([]))
    
    def test_same_many_item_list(self):
        self.assertListEqual([2], unique([2,2,2]))
        self.assertListEqual(['a'], unique(['a','a','a','a']))
        self.assertListEqual([''], unique(['','','']))
        self.assertListEqual([[]], unique([[],[],[],[]]))
        self.assertListEqual([{}], unique([{},{},{},{}]))
        self.assertListEqual([()], unique([(),()]))
    
    def test_2same_item_many_order(self):
        self.assertListEqual([1,2], unique([1,2,1,2,1,2,1,2,1,2,1,2]))
        self.assertListEqual(['good','bad'], unique(['good','bad','good','bad','good','bad']))
        self.assertListEqual(['',' '], unique(['',' ','',' ','',' ']))
    
    def test_many_item_unorder(self):
        self.assertListEqual(['a','b','c'], unique(['a','b','c','c','a','b','c','a','b']))
        self.assertListEqual([3,5], unique([3,3,3,3,5,5,3,5,5,3,3]))
        self.assertListEqual([4,'4',[]], unique([4,4,'4',4,[],'4',[],[]]))

    def test_insert_notlist(self):
        with self.assertRaises(TypeError):
            unique(1)
        with self.assertRaises(TypeError):
            unique('a')
        with self.assertRaises(TypeError):
            unique({})
        
    
        

    
 
if __name__ == '__main__':
    unittest.main()