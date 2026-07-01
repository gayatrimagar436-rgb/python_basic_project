import random
import math

try:
    numbers = set()

    for i in range(10):
        num = int(input(f"Enter number {i+1}: "))
        numbers.add(num)

    tup = tuple(numbers)
    print("Tuple:", tup)

    random_nums = random.sample(tup, min(3, len(tup)))
    print("3 Random Numbers:", random_nums)

    total = sum(tup)
    print("Square root of sum:", math.sqrt(total))

except ValueError:
    print("Invalid input!")
except Exception as e:
    print("Error:", e)