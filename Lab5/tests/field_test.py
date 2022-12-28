import unittest

def field(items, *args):
    assert len(args) > 0, "Количество искомых аргументов равно 0"

    lst = []
    if len(args) > 1:
        for item in items:
            yield {arg: item[arg] for arg in args}
    else:
        for item in items:
            yield item[args[0]]

    return lst



class TestField(unittest.TestCase):
    def setUp(self):
        self.goods = [
           {'title': 'Ковер', 'price': 2000, 'color': 'green'},
           {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
        ]

    def test_one_argument(self):
        result = list(field(self.goods, 'title'))
        answer = ['Ковер', 'Диван для отдыха']
        self.assertEqual(result, answer)

    def test_many_arguments(self):
        result = list(field(self.goods, 'title', 'price'))
        answer = [{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}]
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
