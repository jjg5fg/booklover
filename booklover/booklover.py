import pandas as pd

class BookLover:
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

    def __init__(self,name, email, fav_genre):
        self.name=name
        self.email=email
        self.fav_genre=fav_genre
        self.num_books
        self.book_list

    def add_book(self, book_name,rating):
        ''' This function takes a `book name` (string) and `rating` (integer from 0 to 5)'''
        if (self.has_read(book_name))==True:
            return 'The book already has been read and rated please enter a new book'
        else:
            new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)

    def has_read(self,book_name):
        '''
        - This function takes `book_name` (string) as input and determines if the person has read the book.
        '''
           
        if book_name in list(self.book_list.book_name):
            return True
        else:
            return False
        
    def num_book_read(self):
        return(len(self.book_list.book_name))
    
    def fav_books(self):
        '''
        This function takes no parameters and returns the filtered dataframe of the person’s most favorite books. 
        - Books in this list should have a rating > 3.
        '''

        return (self.book_list[self.book_list.book_rating>3].sort_values(by=['book_rating'],ascending=False))


    











