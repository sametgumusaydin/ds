class stack:
    def __init__(self):
        self.top=0
    def push(self,x,arr,top):
        arr[self.top]=x
        top+=1
        self.top=top
    def pop(self,a,top):
        top-=1
        self.top=top
        return a[top]

st=stack()

st_ar=[]
str='53+'
for i in range(len(str)):
    if str[i]=='+':
        b = st.pop(st_ar, st.top)
        a = st.pop(st_ar, st.top)
        st.push(a+b,st_ar,st.top)
        print('a+b='+(a+b))
    elif str[i] == '-':
        b = st.pop(st_ar, st.top)
        a = st.pop(st_ar, st.top)
        st.push(a - b, st_ar, st.top)
        print('a-b=' + (a - b))
    elif str[i] == '*':
        b = st.pop(st_ar, st.top)
        a = st.pop(st_ar, st.top)
        st.push(a * b, st_ar, st.top)
        print('a*b=' + (a * b))
    elif str[i] == '/':
        b = st.pop(st_ar, st.top)
        a = st.pop(st_ar, st.top)
        st.push(a / b, st_ar, st.top)
        print('a/b=' + (a / b))

    if '0' <= str[i]<='9':
        x=int(str[i])-0
        st.push(x,st_ar,st.top)
    print(st.pop(st_ar,st.top))

