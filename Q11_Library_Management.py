class Library:

    def __init__(self):                # store books and availability

        self.books = {
            "Python": "Available",
            "Java": "Available",
            "DBMS": "Available"
        }

    def add_book(self):                # add new book into library

        book = input("Enter Book Name: ")

        self.books[book] = "Available"

        print("Book Added Successfully")

    def issue_book(self):                # issue book if available

        book = input("Enter Book Name to Issue: ")

        if book in self.books:

            if self.books[book] == "Available":

                self.books[book] = "Issued"

                print("Book Issued")

            else:
                print("Book Already Issued")

        else:
            print("Book Not Found")            

    def return_book(self):               # return book and mark available         

        book = input("Enter Book Name to Return: ")

        if book in self.books:

            self.books[book] = "Available"

            print("Book Returned")

        else:
            print("Book Not Found")

    def display_books(self):                # show only available books

        print("\nAvailable Books:")

        for book, status in self.books.items():

            if status == "Available":

                print(book)

library = Library()                #creating object

while True:

    print("\n----- LIBRARY MENU -----")

    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    choice = int(input("Enter Choice: "))                # taking user choice

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.issue_book()

    elif choice == 3:
        library.return_book()

    elif choice == 4:
        library.display_books()

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
