class Book: 
    max_books_allowed = 3 

    def __init__(self, title, book_id, author):
        self.title = title
        self.book_id = book_id
        self.author = author
        self.is_issued = False 

    def display(self):
        print("Title:-", self.title)
        print("Book ID:-", self.book_id)
        print("Author:-", self.author)  

    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print(f"{self.title} has been issued")
        else:
            print(f"{self.title} is already issued")

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print(f"{self.title} has been returned")
        else:
            print(f"{self.title} was not issued")

b1 = Book("Python Basics", 101, "Guido van Rossum")
b2 = Book("Data Structures and Algorithms", 102, "Robert Lafore")
b3 = Book("Operating Systems", 103, "Abraham Silberschatz")

print("-----")
b1.display()
b1.issue_book()
b2.display()
b2.return_book()
b3.display()
b3.return_book()