for num in range(1, 101):
    if num % 15:
        print("FizzBuzz")
    elif num % 3:
        print("Fizz")
    elif num % 5:
        print("Buzz")
    else:
        print(num)