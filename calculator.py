def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

func_dictionary = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

while True:
  number1 = float(input("What's the first number?: "))
  while True:
    for key in func_dictionary:
      print(key)
    func = input("Pick an operation: ")
    number2 = float(input("What's the next number?: "))
    result = func_dictionary[func](number1, number2)
    print(f"{number1} {func} {number2} = {result}")
    while True:
      use_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
      if use_result.lower() == 'y' or use_result.lower() == 'n':
        break
      else:
        print("I didn't understand...")
    if use_result == 'n':
      break
    number1 = result