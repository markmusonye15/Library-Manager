print(">>> Running the CORRECT app.py file")

class Person:
    def __init__(self, name, age, gender, id ):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = id 
        

    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')

person_one = Person ('John Kamau', 30, 'Male', 3445, )
person_two = Person ('Jane Wanjiru', 25, ' Female', 3446, )
person_one.greet()

print(person_one.name, person_one.age, person_one.gender, person_one.id) 

class Student(Person):
    def __init__(self, name, age, course, student_id):
        super().__init__(name, age, course, student_id)
        self.student_id = student_id
        self.course = course

    def greet(self):
        print(f'Hello, my name is {self.name} and I am a student in {self.course} course and my student_id is {self.student_id}.')
student_one = Student ('John Kaanje', 30, 'Computer Science', 4321)
student_one.greet()
print (student_one.name, student_one.course, student_one.student_id)

class Books:
    def __init__(self, title, author, year, isbn, genre, status="Available"):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.genre = genre
        self.status = status

    def display_info(self):
        print(f'Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}, Genre: {self.genre}, Status: {self.status}')

    def update_status(self, new_status):
        valid_statuses = ['Borrowed', 'Misplaced', 'Returned', 'Read']
        if new_status in valid_statuses:
            self.status = new_status
            print(f"Status of '{self.title}' updated to: {self.status}")
        else:
            print(f"Invalid status. Choose from: {', '.join(valid_statuses)}")


book_one = Books('The Great Gatsby', 'F. Scott Fitzgerald', 1925, '9780743273565', 'Fiction')
book_two = Books('To Kill a Mockingbird', 'Harper Lee', 1960, '9780061120084', 'Fiction')

book_one.display_info()
book_one.update_status("Borrowed")
book_one.display_info()

class Librarian(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age, "Librarian", employee_id)
        self.employee_id = employee_id
        self.books = []

    def greet(self):
        print(f'Hello, my name is {self.name} and I am a librarian with employee ID {self.employee_id}.')

    def record_new_book(self, book):
        self.books.append(book)
        print(f"Recorded new book: {book.title}")

    def lend_book(self, title, borrower_name):
        for book in self.books:
            if book.title == title and book.status == "Available":
                book.status = "Borrowed"
                book.borrowed_by = borrower_name
                print(f"{title} has been lent to {borrower_name}.")
                return
        print(f"{title} is not available for lending.")

    def receive_returned_book(self, title):
        for book in self.books:
            if book.title == title and book.status == "Borrowed":
                print(f"{title} returned by {book.borrowed_by}.")
                book.status = "Available"
                book.borrowed_by = None
                return
        print(f"No borrowed record found for {title}.")

    def track_borrowed_books(self):
        print("Currently borrowed books:")
        borrowed = False
        for book in self.books:
            if book.status == "Borrowed":
                print(f"{book.title} (borrowed by {book.borrowed_by})")
                borrowed = True
        if not borrowed:
            print("No books are currently borrowed.")
librarian_one = Librarian('Alice Mwende', 35, 1234)
librarian_one.greet()

book1 = Books("The Alchemist", "Paulo Coelho", 1988, "9780061122415", "Fiction")
book2 = Books("1984", "George Orwell", 1949, "9780451524935", "Dystopian")

librarian_one.record_new_book(book1)
librarian_one.record_new_book(book2)

librarian_one.lend_book("The Alchemist", "John Doe")

librarian_one.track_borrowed_books()

librarian_one.receive_returned_book("1984")

librarian_one.track_borrowed_books()