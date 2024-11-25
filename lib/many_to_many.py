class Author:
    all = []
    @classmethod
    def sign_contract(book, date, royalties):
        pass
    
    @classmethod
    def total_royalties():
        pass
    
    
    def __init__(self,name):
        self.name = name
    
    @classmethod
    def contracts(self):
        pass
    
    @classmethod
    def books(self):
        pass
    
    

class Book:
    
    all = []
    
    def __init__(self, title):
        self.title = title 
    
    def contracts():
        pass
    
    def authors():
        pass



class Contract:
    
    all = []
    
    @classmethod
    def contracts_by_date(cls, date):
        pass
        
    def __init__(self, author, book, date, royalties):
        self.author = author 
        self.book = book 
        self.date = date 
        self.royalties = royalties 
    
    @property
    def date (self):
        return self._date 
    @date.setter
    def date (self, new_date):
        if isinstance(new_date, str):
            self._date = new_date 
        else:
            raise Exception('Not cool man')  
          
    @property
    def author (self):
        return self._author 
    @author.setter
    def author (self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author 
        else:
            raise Exception('Not cool man')
            
    @property
    def book (self):
        return self._book 
    @book.setter
    def book (self, new_book):
        if isinstance(new_book, Book):
            self._book = new_book 
        else:
            raise Exception('Not cool man')
            
    @property
    def royalties (self):
        return self._royalties 
    @royalties.setter
    def royalties (self, book_royalties):
        if isinstance(book_royalties, int):
            self._royalties = book_royalties 
        else:
            raise Exception('Not cool man')