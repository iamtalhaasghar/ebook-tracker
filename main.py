print('Ebook Reading Management System')

books = list() # create an empty book list
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
        books.append(book_name)
    elif choice == 'b':
        # delete book from our database
        pass
    elif choice == 'c':
        # edit book info
        pass
    elif choice == 'd':
        # edit reading status of the book
        pass
    elif choice == 'e':
        # show all books
        for i in books:
            print(i)
    elif choice == 'q':
        #exit(0) this is not a good approach
        user_wants_to_add_more_books = False

print('Thanks for using my software!')