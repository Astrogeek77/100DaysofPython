class Library:
    books = [
        'To Kill a Mockingbird',
        'The Great Gatsby',
        'One Hundred Years of Solitude',
        'Harry Potter and Sorcerous Stone',
        'Fantastic Beasts'
    ]
    lended_books = []
    total_books = 0
    total_lended_books = 0

    def __init__(self):
        self.total_books = len(self.books)
        self.total_lended_books = len(self.lended_books)
        self.get_books()

    def save_books(self):
        try:
            with open('books.txt', 'w') as f:
                f.writelines(self.books, '\n')
        except Exception as e:
            print(e)

    def get_books(self):
        try:
            with open('books.txt', 'r') as f:
                self.books(f.readlines())
        except Exception as e:
            print(e)

    def add_books(self):
        num_book = int(input('Enter how many books you want to add: '))
        try:
            for i in range(num_book):
                new_book_name = input("Enter book name: ")
                self.books.append(new_book_name.title())
                self.total_books += 1

            print('Books added to memory')
            print(f'Updated book list: {self.books}')
            self.save_books()

        except Exception as e:
            print(e)

    def get_all_books(self):
        try:
            if (len(self.books) == 0):
                print("There are no books in library")
                return

            print('---These are all the availabe books in the library---')
            for index, item in enumerate(self.books, start=1):
                print(f'{index} : {item}')
            print("\n")

        except Exception as e:
            print(e)

    def number_of_books(self):
        # count_books = 0
        # for books in self.books:
        #     count_books += 1
        print(
            f'There are {self.total_books} books in Library and {self.total_lended_books} are lended')
        # print(self.total_books == count_books)

    def lend_book(self):
        a = input('Enter which book you want to lend: ').title()
        try:
            if a in self.books:
                self.books.remove(a)
                self.lended_books.append(a)
                total_lended_books += 1
                total_books -= 1
                print(f'The Book {a} has been lended to you.')
                self.save_books()
            else:
                print(f'Sorry the book {a} is not available in Library')
        except Exception as e:
            print(e)

    def submit_book(self):
        try:
            a = input('Enter which book you are returning: ')
            if a in self.lended_books:
                self.books.append(a)
                self.lended_books.remove(a)
                total_lended_books -= 1
                total_books += 1
                self.save_books()
            else:
                print(f"The book {a} has not been lended by anyone currently.")
            print(f'Thanks for returning the book {a}')
        except Exception as e:
            print(e)

    def delete_book(self):
        try:
            a = input("Enter the book you want to delete: ")
            if a in self.books:
                self.books.remove(a)
                total_books -= 1
                print(f"The book {a} has been deleted.")
                self.save_books()
            elif a in self.lended_books:
                print(
                    f"Unable to delete book {a}, it is currently being lended by someone.")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print('--------------------WELCOME----------------------')
    while True:
        print(
            '[1] to add book\n[2] to get all books\n[3] to get number of books\n[4] to borrow a book\n[5] to submit book\n[6] to delete a book\n[q] to exit'
        )
        user_input = input('Enter your choice: ')
        if user_input == '1':
            lib = Library()
            lib.add_books()

        elif user_input == '2':
            lib = Library()
            lib.get_all_books()

        elif user_input == '3':
            lib = Library()
            lib.number_of_books()

        elif user_input == '4':
            lib = Library()
            lib.lend_book()

        elif user_input == '5':
            lib = Library()
            lib.submit_book()

        elif user_input == '6':
            lib = Library()
            lib.delete_book()

        elif user_input == 'q':
            print('Thanks for using our LMS')
            break

        else:
            print('Invalid Input')
            break
