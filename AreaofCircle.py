__author__ = 'prasadmodi'
class Circle:
    def __init__(self):
        self.raidus = 5
        self.pi = 3.14
    def area(self):
        print('Area of circle: ', self.pi*self.raidus*self.raidus)

    def perimeter(self):
        print("Perimeter of Circle: ", 2 * self.pi * self.raidus)
if __name__ == '__main__':
    C = Circle()
    C.area()
    C.perimeter()