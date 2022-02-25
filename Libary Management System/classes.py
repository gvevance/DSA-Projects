# classes

class book :
    
    ''' Every book has a name,author,genre,price and summary. Some books are included in a 
    particular user membership type, some are not. Can include a sample of the book if needed.
    '''
    def __init__(self) -> None:
        self._title = "Dummy title"
        self._authors = ["Dummy author 1"]
        self._genre = "Romance"
        self._price = 100
        self._summary = "Dummy summary"
    
    def get_title(self) :
        return self._title

    def get_author(self) :
        return self._author

    def get_price(self) :
        return self._price

    def get_summary(self) :
        return self._summary


        