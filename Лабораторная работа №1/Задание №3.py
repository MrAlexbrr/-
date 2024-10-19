# TODO Найдите количество книг, которое можно разместить на дискете
# Данные из задачи
disk_size_mb = 1.44  # размер дискеты в Мб
pages_in_book = 100  # количество страниц в книге
lines_per_page = 50  # число строк на странице
symbols_per_line = 25  # количество символов в строке
bytes_per_symbol = 4  # для хранения кода одного символа нужно 4 байта

# Перевод размера дискеты в байты (1 Мб = 1024 * 1024 байта)
disk_size_bytes = disk_size_mb * 1024 * 1024

# Рассчитаем объем одной книги в байтах
book_size_bytes = pages_in_book * lines_per_page * symbols_per_line * bytes_per_symbol

# Рассчитаем количество книг, которые можно разместить на дискете
number_of_books = int(disk_size_bytes // book_size_bytes)

number_of_books

print("Количество книг, помещающихся на дискету:", number_of_books)
