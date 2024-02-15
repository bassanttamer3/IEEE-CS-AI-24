def create_library_catalogue(limit):
    library_catalogue = {}
    count = 0
    while count < limit:
        title = input("Enter the title of the book : ")
        if title.lower() == 'quit':
            break
        author = input("Enter the author of the book: ")
        publication_year = input("Enter the publication year of the book: ")
        book_details = {"title": title, "author": author, "publication_year": publication_year}
        library_catalogue[title] = book_details
        count += 1
    return library_catalogue


if __name__ == "__main__":
    print("Welcome to the library catalogue creator!")
    limit = int(input("Enter the limit for adding books: "))
    library_catalogue = create_library_catalogue(limit)
    print("\nLibrary Catalogue:")
    for title, details in library_catalogue.items():
        print(f"Title: {title}")
        print(f"Author: {details['author']}")
        print(f"Publication Year: {details['publication_year']}")
        print()
