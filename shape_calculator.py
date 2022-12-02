class Rectangle:
    def __init__(self,width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'
    
    def set_width(self, valor):
        self.width = valor
    def set_height(self, valor):
        self.height = valor
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return (2*self.width) + (2*self.height)
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        p = ''
        if self.height >50 or self.width >50:
            p += 'Too big for picture.'
            return p
        for i in range(0,self.height):
            p += '*'*self.width+'\n'
        return p
    def get_amount_inside(self, obg):
        amount = int(self.get_area() / obg.get_area())
        
        if amount < 1:
            return 0
        elif amount == 1:
            return amount
        elif amount > 1:
            return amount
            
        

class Square(Rectangle):
    def __init__(self, lado):
        self.width = lado
        self.height = lado
    
    def set_side(self, lado):
        self.width = lado
        self.height = lado
    def __str__(self):
        return f'{self.__class__.__name__}(side={self.width})'
    
    

r1 = Rectangle(10, 10)
r2 = Square(5)
print(r1)
print(r2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.get_picture())  
r2.set_side(2)
print(r2.get_picture())
print(r1.get_amount_inside(r2))  


