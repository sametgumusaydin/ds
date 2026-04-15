
def move(n,a,b,c,):
    if n==1:
        print(a+'-->'+b)
    else:
        return move(n-1,a,c,b),move(1,a,b,c), move(n-1,c,b,a)
move(64,'A','B','C')
