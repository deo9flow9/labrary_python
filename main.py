import json
import os

def searchIndexBook(books, index):
    for book in books:
        if(book[0] == index):
            return book
    return None

def rewriteBooks(books):
    if (len(books) == 0):
        print("You need to add books in list")
        return False
    with open('test.json', 'a', encoding='utf-8') as testfile:
        json.dump(books, testfile)

def readBooks():
    with open('test.json', 'r', encoding='utf-8') as testfile:
        try:
            data = json.load(testfile)
        except json.decoder.JSONDecodeError:
            data = []
        return data;

def addBook(books):
    print("Adding book to library")
    title = None
    author = None
    year = None
    while True:
        if (title == None):
            title = input("Please, enter title of book (if you want to cancel, push ENTER): ")
            if (title == ""):
                return False
        if (author == None):
            author = input("Please, enter author of book: ")
        if (year == None):
            temp = input("Please, enter year of book: ")
            try:
                year = int(temp)
            except ValueError:
                print("Not valid year of book")
                continue
        break
    if(len(books) > 0):
        index = books[len(books) - 1][0] + 1
    else:
        index = 0
    books.append([index, title, author, year, True])
    return True

def removeBook(books):
    if (len(books) == 0):
        print("You need to add books in list")
        return False
    print("Removing book from library")
    book = None
    index  = None
    while True:
        temp = input("Please, enter index of book (if you want to cancel method, push ENTER): ")
        if (temp == ""):
            return False
        try:
            index = int(temp)
        except ValueError:
            print("Value is not number")
            continue
        book = searchIndexBook(books, index)
        if(not book):
            print("Index not found in library")
            continue
        break
    del books[index]
    return True


def searchBook(books):
    if (len(books) == 0):
        print("You need to add books in list")
        return False
    print("Searching book from library")
    while True:
        temp = input("Which method of search book to use? (push enter - exit from method, 1 - search by title, 2 - search by author, 3 - search by year): ")
        if (temp == ""):
            return False
        try:
            searchMethod = int(temp)
        except ValueError:
            print("# of method is not correct")
            continue
        if(searchMethod < 0 or searchMethod >= 4):
            continue
        break
    def findBook(books, fieldSearch, value):
        resultOfSearch = []
        for book in books:
            if (book[fieldSearch] == value):
                resultOfSearch.append(book)
        return resultOfSearch
    book = None
    if(searchMethod == 1):
        while True:
            temp = input("Please, enter title of book (if you want to cancel method, push ENTER): ")
            if (temp == ""):
                return False
            book = findBook(books, 1, temp)
            if(not book):
                print("Sorry, we can't find your book by title")
                continue
            break
    elif(searchMethod == 2):
        while True:
            temp = input("Please, enter author of book (if you want to cancel method, push ENTER): ")
            if (temp == ""):
                return False
            book = findBook(books, 2, temp)
            if(not book):
                print("Sorry, we can't find your book by author")
                continue
            break
    elif(searchMethod == 3):
        year = None
        while True:
            temp = input("Please, enter year of book (if you want to cancel method, push ENTER): ")
            if (temp == ""):
                return False
            try:
                year = int(temp)
            except ValueError:
                print("Not valid year of book")
                continue
            book = findBook(books, 3, year)
            if(not book):
                print("Sorry, we can't find your book by year")
                continue
            break
    print(book)
    return True

def printBooks(books):
    if (len(books) == 0):
        print("You need to add books in list")
        return False
    print("Printing data of book from library")
    for book in books:
        print("index: %d, title: %s, , author: %s, year: %d, status: %s" % (book[0], book[1], book[2], book[3], "в наличии" if book[4] else "выдана"))
    return True

def changeStatus(books):
    if (len(books) == 0):
        print("You need to add books in list")
        return False
    print("Change status of book from library")
    book = None
    index  = None
    while True:
        temp = input("Please, enter index of book (if you want to cancel method, push ENTER): ")
        if (temp == ""):
            return False
        try:
            index = int(temp)
        except ValueError:
            print("Value is not number")
            continue
        book = searchIndexBook(books, index)
        if(not book):
            print("Index not found in library")
            continue
        break
    books[index][4] = not books[index][4]
    return True

books = readBooks()
print("Hello in system of managing of library")
while True:
    print("Print action number which you want to use")
    print("press ENTER - exit from console")
    print("1 - Add book")
    print("2 - Remove book")
    print("3 - Search book")
    print("4 - Show all books")
    print("5 - Change status of book")
    print("6 - Save data in library")
    temp = input(">> ")
    if (temp == ""):
        break
    try:
        index = int(temp)
    except ValueError:
        print("Value is not number")
        continue
    if (index == 1):
        addBook(books)
    elif(index == 2):
        removeBook(books)
    elif(index == 3):
        searchBook(books)
    elif(index ==4):
        printBooks(books)
    elif(index == 5):
        changeStatus(books)
    elif(index == 6):
        rewriteBooks(books)
    else:
        print("Wrong action number. Print another")
        continue
print("See you soon!")
