import json

class BookCollection:
    """Manage a personal collection of books with file storage and user interaction."""

    def __init__(self):
        """
        Initialize the book collection.

        Loads existing books from file, or starts with an empty list if file not found.
        """
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """
        Read the list of books from the storage file.

        If the file doesn't exist or contains invalid JSON, initializes with an empty list.
        """
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
            print(self.storage_file)
            print(self.book_list)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """
        Save the current book list to the storage file in JSON format.
        """
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """
        Prompt the user for book details and add the new book to the collection.
        """
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        publish_year = input("Enter publish year: ")
        genre = input("Enter book genre: ")
        is_read = (input("Have you ever read this book? [yes/no] ").lower().strip() == "yes")

        new_book = {
            "title": title,
            "author": author,
            "year": publish_year,
            "genre": genre,
            "read": is_read
        }

        self.book_list.append(new_book)
        self.save_to_file()

        print("Book has been added successfully!")

    def delete_book(self):
        """
        Delete a book from the collection by title.
        """
        book_title = input("Enter the title of the book to delete: ").lower()
        for book in self.book_list:
            if book["title"].lower() == book_title:
                self.book_list.remove(book)
                self.save_to_file()
                print("Book has been deleted successfully.")
                return
        print("Book not found!")

    def find_book(self):
        """
        Search for books by title or author and display the matching results.
        """
        search_term = input("Enter book title or author name: ").lower()
        found_books = [
            book for book in self.book_list
            if search_term in book["title"].lower() or search_term in book["author"].lower()
        ]
        if found_books:
            print("Matching Books:")
            for index, book in enumerate(found_books, 1):
                read_status = "Read" if book["read"] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
        else:
            print("No matching book found!")

    def show_all_books(self):
        """
        Display all books in the collection.
        """
        if not self.book_list:
            print("Your library is empty!")
            return
        print("Your Books Collection:")
        for index, book in enumerate(self.book_list, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

    def show_progress(self):
        """
        Show the number of books read out of total and the reading completion rate.
        """
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0

        print(f"\nReading Progress:")
        print(f"Books Read: {completed_books}/{total_books}")
        print(f"Completion Rate: {completion_rate:.2f}%\n")

    def start_app(self):
        """
        Start the interactive menu-driven interface for managing the book collection.
        """
        while True:
            print("\n📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. View all books")
            print("5. View reading progress")
            print("6. Exit")
            user_choice = input("Please choose an option (1-6): ")
            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.show_all_books()
            elif user_choice == "5":
                self.show_progress()
            elif user_choice == "6":
                self.save_to_file()
                print("Thank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("Invalid input. Please choose between 1 and 6.")

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_app()