def outer_func():
  print("Outer")

  def inner_func():
    print("Inner")

  return inner_func

inner_func = outer_func()
inner_func()    