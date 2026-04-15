class ArrayStack:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self._a = [None] * capacity
        self._top = -1

    def push(self, x):
        if self.is_full():
            raise OverflowError("Stack overflow")
        self._top += 1
        self._a[self._top] = x

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        val = self._a[self._top]
        self._a[self._top] = None  # optional: help GC
        self._top -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("peek on empty stack")
        return self._a[self._top]

    def is_empty(self):
        return self._top == -1

    def is_full(self):
        return self._top == len(self._a) - 1

    def size(self):
        return self._top + 1

    def capacity(self):
        return len(self._a)



st = ArrayStack(5)
for i in range(1, 7):
    try:
        st.push(i)
    except OverflowError as e:
        print("overflow:", e)
while not st.is_empty():
    print("pop:", st.pop())
try:
    st.pop()
except IndexError as e:
    print("underflow:", e)