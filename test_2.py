# TODO Найдите количество книг, которое можно разместить на дискете
BT = 1
KB = 1024 * BT
MB = 1024 * KB
amount = 1.44 * MB
one_symbol_weight = 4

weight_one_string = 25 * one_symbol_weight
weight_one_page = 50 * weight_one_string
weight_one_book = 100 * weight_one_page

total_books = amount // weight_one_book

print("Количество книг, помещающихся на дискету:", int(total_books))
