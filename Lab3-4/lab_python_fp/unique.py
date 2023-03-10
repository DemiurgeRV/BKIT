from lab_python_fp.gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.set = set()
        self.iter = iter(items)

    def __next__(self):
        for current in self.iter:
            if self.ignore_case == False:
                if current not in self.set:
                    self.set.add(current)
                    return current
            else:
                if current.lower() not in self.set:
                    self.set.add(current)
                    return current
        raise StopIteration

    def __iter__(self):
        return self

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get("ignore_case", False)
        self.iter = iter(items)
        self.used = set()

    def __next__(self):
        for current in self.iter:
            if isinstance(current, str):
                if (current.lower() if self.ignore_case else current) not in self.used:
                    self.used.add(current.lower())
                    return current
            else:
                if current not in self.used:
                    self.used.add(current)
                    return current
        raise StopIteration

    def __iter__(self):
        return self


def main():


    u = Unique([2, 1, 2, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 4, 5, 4])
    for i in u:
        print(i, end=" ")
    print()
    u = Unique(["A", "a", "B", "b", "b", "B", "A", "C"])
    for i in u:
        print(i, end=" ")
    print()
    u = Unique(["A", "a", "B", "b", "b", "B", "A", "C"], ignore_case=True)
    for i in u:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    print(list(Unique([1, 1, 1, 1, 1, 2, 2, 2, 2, 2])))
    print(list(Unique(gen_random(10, 1, 3))))
    print(list(Unique(['a', 'A', 'b', 'B', 'a', 'b'])))
    print(list(Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'], ignore_case=True)))