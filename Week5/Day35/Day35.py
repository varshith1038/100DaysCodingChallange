# Information about the library
library_name = "Pythonic Library"
library_location = "Cityville"

# List of books available in the library
books = [
    {"title": "Introduction to Python", "author": "John Python", "genre": "Programming"},
    {"title": "Python for Beginners", "author": "Alice Coder", "genre": "Programming"},
    {"title": "Mystery of Pythonic Code", "author": "Sherlock Hacker", "genre": "Mystery"},
]

Task-1
for book in books:
    print(book)

Task-2
for book in books:
    if book["genre"] == "Programming":
        print(f"{book['title']} by {book['author']}")

Task-3
def Staff_info(staff):
    print(staff['librarian'])
library_staff = {
    "librarian": {"name": "Eva Librarian", "age": 35, "role": "Librarian"},
    "assistant": {"name": "Alex Assistant", "age": 28, "role": "Assistant Librarian"},
}
print(Staff_info(library_staff))

Task-4
favorite_genre = input("\nEnter your favorite book genre: ")
genre_books = [book for book in books if book["genre"] == favorite_genre]
if genre_books:
    print(f"\nThe library has the following books in the {favorite_genre} genre:")
    for book in genre_books:
        print(book)
else:
    print(f"\nSorry, the library doesn't have books in the {favorite_genre} genre.") 


