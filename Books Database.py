books_db = {}

while True:
    print("1.Insert")
    print("2.Display all books")
    print("3.Display all authors")
    print("4.Get a author")
    print("5.Delete")
    choice = input("Which on do you want to do? Type your choice number here: ")

    if choice == "1":
        book = input("What book do you want to add: ")
        author = input("What is the author of that book: ")
        books_db[book] = author
        print(books_db)
    elif choice == "2":
        print(books_db.keys())
    elif choice == "3":
        print(books_db.values())
    elif choice == "4":
        the_book = input("What books author do you want: ")
        print(books_db[the_book])
    elif choice == "5":
        to_delete = input("Which book do you want to delete from the dictionary: ")
        del(books_db[to_delete])
        print(books_db)
    else:
        print("Oops.")
        break
