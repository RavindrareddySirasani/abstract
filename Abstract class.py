from ABC import ABC,abstract method
Class Absdemo(ABC):
 @abstractmethod
 def display(self):
  None

Class Demo(Absdemo):
 def display(self):
  Print('concrete class method')
Ob=Demo()
Ob.display()
