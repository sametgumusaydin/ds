class square:
    def __init__(self,a):
        self.a=a
    def calculate_perimeter(self):
        print(4*self.a)
    def calculate_area(self):
        print('square area={}'.format(self.a*self.a))

bikare=square(8)
bikare.calculate_perimeter()
bikare.calculate_area()