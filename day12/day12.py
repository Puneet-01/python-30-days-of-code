from abc import ABC, abstractmethod
class Book(ABC):
    @abstractmethod
    def display():
        pass
class Mybook(Book):
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)
t=input()
a=input()
p=int(input())
ob=Mybook(t,a,p)
ob.display()