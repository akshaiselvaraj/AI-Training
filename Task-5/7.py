class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  

    def borrow_book(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully.")
        else:
            print("Sorry, book is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully.")
        else:
            print("Book was not borrowed.")

    def display_status(self):
        status = "Available" if self.available else "Not Available"
        print("\nTitle:", self.title)
        print("Author:", self.author)
        print("Status:", status)

title = input("Enter book title: ")
author = input("Enter author name: ")

book = Book(title, author)

while True:
    print("\n1. Borrow Book")
    print("2. Return Book")
    print("3. Display Status")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        book.borrow_book()

    elif choice == '2':
        book.return_book()

    elif choice == '3':
        book.display_status()

    elif choice == '4':
        print("Thank you!")
        break

    else:
        print("Invalid choice")
