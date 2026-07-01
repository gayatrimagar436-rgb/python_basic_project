square = lambda x: x * x

try:
    numbers = list(range(1, 21))
    squares = list(map(square, numbers))

    even_squares = [x for x in squares if x % 2 == 0]

    print("Squares:", squares)
    print("Even Squares:", even_squares)

except Exception as e:
    print("Error:", e)