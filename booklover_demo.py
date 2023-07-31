from booklover import booklover

test_object = booklover.BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
test_object.add_book("War of the Worlds", 4)
test_object.add_book('Book1',2)
print(test_object.has_read('Book1'))
print(test_object.add_book('Book1',5))
print(test_object.num_book_read())
print(test_object.fav_books())


