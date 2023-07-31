import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        bl1= BookLover('Jack','abc@123.com','nonfiction')
        bl1.add_book('book1',5)
        bl1.add_book('book2',5)
        expected=['book1','book2']
        self.assertEqual(list(bl1.book_list.book_name), expected)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        bl1= BookLover('Jack','abc@123.com','nonfiction')
        bl1.add_book('book1',5)
        bl1.add_book('book1',5)
        expected=['book1']
        self.assertEqual(list(bl1.book_list.book_name), expected)


                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        bl1= BookLover('Jack','abc@123.com','nonfiction')
        bl1.add_book('book1',5)
        self.assertTrue(bl1.has_read('book1'))
        
    
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bl1= BookLover('Jack','abc@123.com','nonfiction')
        bl1.add_book('book1',5)
        self.assertFalse(bl1.has_read('book2'))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        bl1= BookLover('Jack','abc@123.com','nonfiction')
        bl1.add_book('book1',5)
        bl1.add_book('book2',5)
        expected=2
        self.assertEqual(bl1.num_book_read(), expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3

        bl1= BookLover('Jack','abc@123.com','nonfiction')
        bl1.add_book('book1',5)
        bl1.add_book('book2',2)
        bl1.add_book('book3',4)
        bl1.add_book('book4',3)
        bl1.add_book('book5',3.5)
        self.assertTrue(all(x>3 for x in bl1.fav_books().book_rating))
    
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
