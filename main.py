from models.Books import db
print('Ebook Reading Management System')
user_wants_to_add_more_books = True
while user_wants_to_add_more_books:
    main_menu = '''
    a) Enter new book
    b) Delete existing book
    c) Edit existing book
    d) Edit Reading Status
    e) Show all books
    q) quit program
    '''
    print(main_menu)
    choice = input('a/b/c/d/e/q>') # we are assuming that user is intelligent and will not enter anything beside valid choices given
    # do something based on your choice
    if choice == 'a':
        # add a book to our database
        book_name = input('Enter book name:')
        author_name = input('Enter author name:')
        db.books.insert(name=book_name, author= author_name)
        db.commit()
    elif choice == 'b':
        # delete a book
        books = db(db.books).select()
        for book in books:
            print(book.id, ')', book.name, ' by ', book.author)
        book_id = int(input('Enter book id to delete: '))
        db(db.books.id == book_id).delete()
        db.commit()
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
        books = db(db.books).select()
        for book in books:
            print(book.id, ')', book.name, ' by ', book.author)
    elif choice == 'q':
        user_wants_to_add_more_books = False
print('Thanks for using my software!')