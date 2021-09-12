"""Yandex chained list interview task.
Condition:
You need to write down a function which receives the first element of chained list.
Function should reverse it and return new first element of chained list. """


class ChainedElem:
    """Single element of chained list. If it's the last element next_elem is None."""
    def __init__(self, value, next_elem=None):
        self.value = value
        self.next_elem = next_elem

    def __str__(self):
        return f'{self.value}, next - {self.next_elem.value}'

    def __call__(self):
        print(self)


d = ChainedElem('D')
c = ChainedElem('C', next_elem=d)
b = ChainedElem('B', next_elem=c)
a = ChainedElem('A', next_elem=b)



def create_chained_list(*args):
    chained = None
    for elem in args[::-1]:
        _next = chained
        chained = ChainedElem(elem, _next)
    return chained

example = create_chained_list('A', 'B', 'C')
example()