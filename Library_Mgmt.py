class Library:
    
    def __init__(self,listOfBooks):
        self.books=listOfBooks

    def displayAvailableBook(self):
        print("Books Present in this Library are: ")
        for books in self.books:
            print(books)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"Book {bookName} is issued")
            self.books.remove(bookName)
        else:
            print("Book {bookname} is not present or issued to someone else")        
    
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning the Book")
    
class Student:
    def requestBook(self):
        a=input("Enter the name of the book you want to borrow: ")
        return a
    def returnBook(self):
        b=input("Enter the name of the book you want to return: ")
        return b

if __name__ == "__main__":
    centralLibrary=Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student=Student()

    while(True):
        welcomeMsg = ''' ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)

        a=int(input("Enter Your Choice: "))
        if a==1:
            centralLibrary.displayAvailableBook()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for using Central Library")
            exit()
        else:
            print("Invalid Input")