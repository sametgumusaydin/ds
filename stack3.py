class stack2:
    def __init__(self):
        self.top = 0
    def push(self, x, arr, top):
        arr[self.top] = x
        top += 1
        self.top = top
    def pop(self, a, top):
        if self.top == 0:
            raise IndexError("pop from empty stack")
        top -= 1
        self.top = top
        return a[top]
st = stack2()
expr = '532-/47*+'
st_ar = [0] * len(expr)  # ÖNEMLİ: push arr[self.top] yazdığı için önceden yer ayır

for i in range(len(expr)):
    ch = expr[i]
    if '0' <= ch <= '9':
        x = int(ch)
        st.push(x, st_ar, st.top)

    elif ch == '+':
        b = st.pop(st_ar, st.top)
        a = st.pop(st_ar, st.top)
        st.push(a + b, st_ar, st.top)
        print('a+b =', (a + b))

    elif ch == '-':
        b = st.pop(st_ar, st.top)
        a = st.pop(st_ar, st.top)
        st.push(a - b, st_ar, st.top)
        print('a-b =', (a - b))
    elif ch == '*':
        b = st.pop(st_ar, st.top)
        a = st.pop(st_ar, st.top)
        st.push(a * b, st_ar, st.top)
        print('a*b =', (a * b))
    elif ch == '/':
        b = st.pop(st_ar, st.top)
        a = st.pop(st_ar, st.top)
        if b == 0:
            raise ZeroDivisionError("0'a bölme")
        st.push(a / b, st_ar, st.top)
        print('a/b =', (a / b))

# Sonuç (stack'in tepesindeki değer)
print("Postfix sonucu =", st.pop(st_ar, st.top))
