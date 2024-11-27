class Triangle:
    def __init__(self):
        try:
            print("Hello!")
            self.n=int(input("Enter the Height of triangle : "))
            if self.n<=0:
                raise Exception
        except:
            b=False
            while b==False:
                try:
                    print( "Height should be a Integer Greater than zero Only !")
                    self.n=int(input("Enter Height again : "))
                    if self.n<=0:
                        raise Exception
                    b=True
                except:
                    continue


        self.s=input("Enter the String from which the Triangle is to be made :\n")

    def leftSide(self):
        for i in range(1,self.n+1):
            print(self.s*i)
    def rightSide(self):
        for i in range(1,self.n+1):
            print((self.n-i)*' '+self.s*i)
    def center(self):
        for i in range(1,self.n+1):
            print((self.n-i)*' '+self.s*(i-1)+self.s*(i))
obj=Triangle()

ch=int(input("Enter 1 for a Right Angled Triangle on Left Side.\nEnter 2 for a Right Angled Triangle on Right Side. \nEnter 3 for a Isosceles Triangle.\n  Enter your choice : "))
if ch==1:
    obj.rightSide()
if ch==2:
    obj.leftSide()
if ch==3:
    obj.center()