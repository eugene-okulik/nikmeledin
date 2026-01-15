class Book:
    """Описание книги"""
    def __init__(self, book_title, author, num_of_pages, ISBN, reserved):
        """Свойства книги"""
        self.book_title = book_title
        self.author = author
        self.num_of_pages = num_of_pages
        self.ISBN = ISBN
        self.reserved = reserved
        self.page_material = 'Бумага'
        self.text = True


book1 = Book('451 градус по Фаренгейту', 'Рэй Брэдбери', 300, '123456', False)
book2 = Book('Тихий Дон', 'Михаил Шолохов', 200, '654321', False)
book3 = Book('Гордость и предубеждение', 'Джейн Остин', 452, '112233', False)
book4 = Book('Маленький принц', 'Антуан де Сент-Экзюпери', 157, '445566', False)
book5 = Book('Робинзон Крузо', 'Даниэль Дефо', 347, '778899', True)


def print_book(book):
    if book.reserved:
        return (f"Название: {book.book_title}, Автор: {book.author}, страниц: {book.num_of_pages}, материал: {book.page_material}, зарезервирована")
    else:
        return (f"Название: {book.book_title}, Автор: {book.author}, страниц: {book.num_of_pages}, материал: {book.page_material}")


print(print_book(book1))
print(print_book(book5))


class Textbooks(Book):
    """Описание школьных учебников"""
    def __init__(self, book_title, author, num_of_pages, ISBN, reserved, subject, school_class, availability_of_assignments):
        """Свойства учебника"""
        super().__init__(book_title, author, num_of_pages, ISBN, reserved)
        self.subject = subject
        self.school_class = school_class
        self.availability_of_assignments = availability_of_assignments


textbook1 = Textbooks('Алгебра', 'Иванов', 200, '999888', False, 'Математика', 9, True)
textbook2 = Textbooks('История России', 'Петров', 150, '777666', True, 'История', 8, False)


def print_textbook(book):
    if book.reserved:
        return (f"Название: {book.book_title}, Автор: {book.author}, страниц: {book.num_of_pages}, предмет: {book.subject}, класс: {book.school_class}, зарезервирован")
    else:
        return (f"Название: {book.book_title}, Автор: {book.author}, страниц: {book.num_of_pages}, предмет: {book.subject}, класс: {book.school_class}")


print(print_textbook(textbook1))
print(print_textbook(textbook2))
