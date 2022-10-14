def logging_decorator(func):
  def wrapper(*args):
    print(func.__name__, args)
  return wrapper  

@logging_decorator
def my_func():
  print(f"initiating function! ")

my_func("stuffff", "blep", 2, 3, 5, 7)  