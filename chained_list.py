"""Yandex chained list interview task.
Condition:
You need to write down a function which receives the first element of chained list.
Function should reverse it and return new first element of chained list. """


class ChainedElem:
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

    def __add__(self, other):
        if isinstance(other, ChainedElem):
            raise ValueError('You cannot add ChainedElem as value of new chained elem!')
        return ChainedElem(value=other, next_elem=self)

    def __len__(self):
        a, count = self, 0
        while a is not None:
            print(a)
            a = a.next_elem
            count += 1
        return count


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


# example = reverse_chained_list(example)

_new = example + 1 + 2 + 3
# _new()
print(len(_new))
