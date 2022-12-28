import unittest
from random import randint


def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield randint(begin, end)

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.iter = iter(items)
        self.used = set()

    def __next__(self):
        for current in self.iter:
            if (current.lower() if self.ignore_case else current) not in self.used:
                self.used.add(current)
                return current
        raise StopIteration

    def __iter__(self):
        return self
class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.iter = iter(items)
        self.used = set()

    def __next__(self):
        for current in self.iter:
            if (current.lower() if self.ignore_case else current) not in self.used:
                self.used.add(current)
                return current
        raise StopIteration

    def __iter__(self):
        return self

class TestUnique(unittest.TestCase):
    def test_numbers(self):
        data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        result = list(Unique(data))
        answer = [1, 2]
        self.assertEqual(result, answer)

    def test_random_generator(self):
        data = gen_random(10, 1, 3)
        result = set(Unique(data))
        answer = set(range(1, 4))
        self.assertTrue(answer.issubset(result))

    def test_letters(self):
        data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        result = list(Unique(data))
        answer = ['a', 'A', 'b', 'B']
        self.assertEqual(result, answer)

    def test_letters_ignoring_case(self):
        data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        result = list(Unique(data, ignore_case=True))
        answer = ['a', 'b']
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
