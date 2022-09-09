class Animal:
  def __init__(self) -> None:
    self.num_eyes = 2

  def breathe(self):
    print("HHhhhhHHhhHHHhhh")  



# Syntax for inheriting from another class
class Fish(Animal):
  def __init__(self) -> None:
    # Trigger the super class (Animal) to inherit all attributes and methods from the parent class
    super().__init__()

  def breathe(self):
    super().breathe()
    print("I am in the fish class Breathing")

  def swim(self):
    print("Swimming wimmmsdingngngnsdfsdf")

nemo = Fish()
nemo.swim()
nemo.breathe()