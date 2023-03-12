from models.Books import db
import os, time
print('Ebook Reading Management System')
user_wants_to_add_more_books = True
os.system('color 3F')
while user_wants_to_add_more_books:
    os.system('clear')
    main_menu = '''
    a) Enter new book
    b) Delete existing book
    c) Edit existing book
    d) Edit Reading Status
    e) Show all books
    q) quit program
    '''
    print(main_menu)
    choice = input('a/b/c/d/e/q> ') # we are assuming that user is intelligent and will not enter anything beside valid choices given
    # do something based on your choice
    if choice == 'a':
        # add a book to our database
        os.system('clear')
        print('# Enter a new book\n\n')
        book_name = input('Enter book name:')
        author_name = input('Enter author name:')
        db.books.insert(name=book_name, author= author_name)
        db.commit()
        print('Your book was inserted successfully!')
    elif choice == 'b':
        # delete a book
        os.system('clear')
        print('# Delete a book\n\n')
        books = db(db.books).select()
        for book in books:
            print(book.id, ')', book.name, ' by ', book.author)
        book_id = int(input('Enter book id to delete: '))
        db(db.books.id == book_id).delete()
        db.commit()
        print('Your book was deleted successfully!')
    elif choice == 'c':
        # edit book info
        books = db(db.books).select()
        for book in books:
            print(book.id, ')', book.name, ' by ', book.author)
        book_id = int(input('Enter book id to edit: '))
        book_name = input('Enter new book name: ')
        db(db.books.id == book_id).update(name=book_name)
        db.commit()
    elif choice == 'd':
        # edit reading status
        pass
    elif choice == 'e':
        # show all books
        os.system('clear')
        books = db(db.books).select()
        for book in books:
            print(book.id, ')', book.name, ' by ', book.author)
        input('Press any key to go back to main menu...')
    elif choice == 'q':
        user_wants_to_add_more_books = False
    time.sleep(2)
print('Thanks for using my software!')