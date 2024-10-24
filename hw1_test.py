import data
import hw1
import unittest

from data import Rectangle


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input = "hello"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected,result)

    def test_vowel_count_2(self):
        input = "onomatopoeia"
        result = hw1.vowel_count(input)
        expected = 8
        self.assertEqual(expected,result)

    # Part 2
    def test_short_lists_1(self):
        input = [[1, 2], [1, 2, 3], [4, 5], [6]]
        result = hw1.short_lists(input)
        expected = [[1,2],[4,5]]
        self.assertEqual(expected,result)

    def test_short_lists_2(self):
        input = [[5,1,6],[],[3,67,1,8],[5,1],[-6,8]]
        result = hw1.short_lists(input)
        expected = [[5,1],[-6,8]]
        self.assertEqual(expected,result)

    # Part 3
    def test_ascending_pairs_1(self):
        input = [[5,1,6],[5,1],[],[3,67,1,8],[-6,8]]
        result = hw1.ascending_pairs(input)
        expected = [[5,1,6],[1,5],[],[3,67,1,8],[-6,8]]
        self.assertEqual(expected,result)

    def test_ascending_pairs_2(self):
        input = [[6,1],[2,6,8,2,3],[2,-1],[5,3,1,6],[-15,5]]
        result = hw1.ascending_pairs(input)
        expected = [[1,6],[2,6,8,2,3],[-1,2],[5,3,1,6],[-15,5]]
        self.assertEqual(expected,result)

    # Part 4
    def test_add_prices_1(self):
        input1 = data.Price(15, 68)
        input2 = data.Price(2,12)
        result = hw1.add_prices(input1, input2)
        expected = data.Price(17, 80)
        self.assertEqual(expected, result)

    def test_add_prices_2(self):
        input1 = data.Price(36, 46)
        input2 = data.Price(78,79)
        result = hw1.add_prices(input1, input2)
        expected = data.Price(115, 25)
        self.assertEqual(expected, result)


    # Part 5
    def test_rectangle_area_1(self):
        input = data.Rectangle(data.Point(50,200),data.Point(100,100))
        result = hw1.rectangle_area(input)
        expected = 5000
        self.assertEqual(expected, result)

    def test_rectangle_area_2(self):
        input = data.Rectangle(data.Point(-1000,1000),data.Point(-500,200))
        result = hw1.rectangle_area(input)
        expected = 400000
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author_1(self):
        input1 = "Stephen King"
        input2 = [data.Book("Stephen King", "IT"), data.Book("J.K. Rowling", "Harry Potter"),
                  data.Book("Stephen King", "The Shining")]
        result = hw1.books_by_author(input1, input2)
        expected = [data.Book("Stephen King", "IT"), data.Book("Stephen King", "The Shining")]
        self.assertEqual(expected, result)

    def test_books_by_author_2(self):
        input1 = "William Shakespeare"
        input2 = [data.Book("William Shakespeare", "Hamlet"), data.Book("William Shakespeare", "Romeo and Juliet"),
                  data.Book("Stephen King", "The Shining")]
        result = hw1.books_by_author(input1, input2)
        expected = [data.Book("William Shakespeare", "Hamlet"), data.Book("William Shakespeare", "Romeo and Juliet")]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound_1(self):
        input = data.Rectangle(data.Point(5, 16), data.Point(12, 10))
        result = hw1.circle_bound(input)
        expected = data.Circle(data.Point(8.5, 13.0), 4.61)
        self.assertEqual(expected, result)

    def test_circle_bound_2(self):
        input = data.Rectangle(data.Point(-10, 56), data.Point(15, 12))
        result = hw1.circle_bound(input)
        expected = data.Circle(data.Point(2.5, 34.0), 25.3)
        self.assertEqual(expected, result)

    # Part 8
    def test_below_pay_average_1(self):
        input = [data.Employee("Charles", 20000),
                 data.Employee("Dillon", 50000),
                 data.Employee("Bobby", 10000),
                 data.Employee("Jonas", 60000)]
        result = hw1.below_pay_average(input)
        expected = ["Charles", "Bobby"]
        self.assertEqual(expected, result)

    def test_below_pay_average_2(self):
        input = [data.Employee("Cash", 30000),
                 data.Employee("Donnie", 40000),
                 data.Employee("Lucas", 30000),
                 data.Employee("Scotty", 30000)]
        result = hw1.below_pay_average(input)
        expected = ["Cash", "Lucas", "Scotty"]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
