# def my_func(*args):
#     return args


# vars = my_func("aaaa", "beee", 7)
# print(vars)

# def add(*nums):
#   total = 0
#   for num in nums:
#     total += num
#   return total

# my_total = add(5, 6, 7, 8, 9, 90)
# print(my_total)

# **kwargs - Keyword Arguments


from pyexpat import model


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
    print(kwargs["add"])
    print(kwargs["multiply"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(10, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # get method will assign the passed in argument's value, if no value exists, it will return None, avoiding Errors
        self.make = kw.get("make")
        self.model = kw.get("model")
        # self.make = kw["make"]
        # self.model = kw["model"]


my_car = Car(make="Honda", model="Civic") 
my_second_car = Car(make="Toyota") 
print(my_car.make, my_car.model) # Honda Civic
print(my_second_car.make, my_second_car.model) # Toyota None
