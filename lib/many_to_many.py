class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        new_Contract = Contract(self, book, date, royalties)
        return new_Contract

    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])

class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("Author must be an author obj")
        self.author = author
        if not isinstance(book, Book):
            raise ValueError("Book must be an book obj")
        self.book = book
        if not isinstance(date, str):
            raise ValueError("date must be a str")
        self.date = date
        if not isinstance(royalties, int):
            raise ValueError("royalties must be a int")
        self.royalties = royalties

        Contract.add_new_contract(self)
        
    @classmethod
    def add_new_contract(cls, new_contract):
        cls.all.append(new_contract)
    
    @classmethod
    def contracts_by_date(cls, new_date):
        return [contract for contract in cls.all if contract.date == new_date]