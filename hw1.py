import data
from data import Rectangle


# Write your functions for each part in the space below.

# Part 1
def vowel_count(word:str) -> int:
    count = 0
    vowels = ['a','e','i','o','u']
    for letter in word:
        if letter in vowels:
            count += 1
    return count


# Part 2
def short_lists(list1:list[list[int]]) -> list:
    shortl = []
    for list2 in list1:
        if len(list2) == 2:
            shortl.append(list2)
    return shortl

# Part 3
def ascending_pairs(list1:list[list[int]])-> list:
    new_list = []
    for lists in list1:
        if len(lists) == 2:
            temp = ""
            if lists[0] > lists[1]:
                temp = lists[1]
                lists[1] =lists[0]
                lists[0] = temp
        new_list.append(lists)
    return new_list


# Part 4
def add_prices(price1:data.Price, price2:data.Price) -> data.Price:
    dollar_sum = price1.dollars + price2.dollars
    cents_sum = price1.cents + price2.cents
    dollar_remainder = cents_sum//100
    sum_price = data.Price(dollar_sum + dollar_remainder, cents_sum%100)
    return sum_price


# Part 5
def rectangle_area(rectangle1:data.Rectangle) -> float:
    x1 = rectangle1.bottom_right.x
    x2 = rectangle1.top_left.x
    y1 = rectangle1.top_left.y
    y2 = rectangle1.bottom_right.y
    width = x1 - x2
    length = y1 - y2
    return width * length

# Part 6
def books_by_author(author:str, books:list[data.Book]) -> list[data.Book]:
    author_book = []
    for book in books:
        if book.authors == author:
            author_book.append(book)
    return author_book

# Part 7
def circle_bound(rectangle1:data.Rectangle) -> data.Circle:
    x1 = rectangle1.bottom_right.x
    x2 = rectangle1.top_left.x
    y1 = rectangle1.top_left.y
    y2 = rectangle1.bottom_right.y
    width = x1 - x2
    length = y1 - y2
    radius = 0
    if width < length:
        radius = width / 2
    else:
        radius = length / 2
    center = data.Point((x1 + x2)/2, (y1 + y2)/2)
    return data.Circle(center, radius)

# Part 8
def below_pay_average(all_employees:list[data.Employee]) -> list[str]:
    sum = 0
    low_pay_rate_employees = []
    for employee in all_employees:
        sum += employee.pay_rate
    average = sum/len(all_employees)
    for employee in all_employees:
        if employee.pay_rate < average:
            low_pay_rate_employees.append(employee.name)
    return low_pay_rate_employees