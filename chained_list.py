"""Yandex chained list interview task.
Condition:
You need to write down a function which receives the first element of chained list.
Function should reverse it and return new first element of chained list. """


class ChainedElem(list):  # TODO Create child class that has __str__ method which is recursive. That class must be created
    # from parent.
    """Single element of chained list. If it's the last element next_elem is None."""
    def __init__(self, value, next_elem=None):
        self.value = value
        self.next_elem = next_elem

    def __repr__(self):
        try:
            return f'{self.value}, next - {self.next_elem.value}'
        except AttributeError:
            return f'{self.value}'

    def __call__(self):
        print(self)


    def __add__(self, x):
        self.insert(0, x)
        print(self[0])



class ChildChainedElem(ChainedElem):

    def __init__(self, value, next_elem=None):
        self.value = value
        self.next_elem = next_elem

    def __str__(self):
        print(f'value = {self.value}, next elem = {self.next_elem}.')

    # TODO make __add__ method that adds new element in chained list in front of first and returns new first element
    # TODO make __len__ method that returns count of elements of chained list


def create_chained_list(*args):
    chained = None
    for elem in args[::-1]:
        _next = chained
        chained = ChainedElem(elem, _next)
    return chained


example = create_chained_list('A', 'B', 'C', 'D')


def reverse_chained_list(first: ChainedElem) -> ChainedElem:
    left, right = None, first
    while True:
        print(f'{left = }, {right = }')
        elem = right.next_elem
        print(f'{elem = }')
        right.next_elem = left
        if not elem:
            return right
        left = right
        right = elem


reverse_chained_list(example)()

example.__add__('E')
