import jsonpath
import json

obj = json.load(open('book.json', 'r', encoding='utf8'))
print(obj)

# 所有的title
author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(author_list)

author_all = jsonpath.jsonpath(obj, '$..author')
print(author_all)

# store下面所有的元素
tag_list = jsonpath.jsonpath(obj, '$.store.*')
print(tag_list)

# store下的所有东西的price
price_list = jsonpath.jsonpath(obj, '$.store..price')
print(price_list)
price_list = jsonpath.jsonpath(obj, '$..price')
print(price_list)

# 第三本书
third_book = jsonpath.jsonpath(obj, '$..book[2]')
print(third_book)

# 最后一本书
end_book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
print(end_book)

# 前两本书
sec_book_list = jsonpath.jsonpath(obj, '$..book[0,1]')
print(sec_book_list)
sec_book_list = jsonpath.jsonpath(obj, '$..book[:2]')
print(sec_book_list)

# 过滤出所有包含isbn的书
has_isbn_book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print(has_isbn_book_list)

# 超过10块钱的书
more_10_book_list = jsonpath.jsonpath(obj, '$..book[?(@.price > 10)]')
print(more_10_book_list)