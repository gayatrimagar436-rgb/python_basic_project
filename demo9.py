import math

try:
    sentence = input("Enter a sentence: ")

    words = sentence.split()
    unique_words = sorted(set(words))

    print("Unique Words:", unique_words)

    count = len(unique_words)
    print("Square of total unique words:", math.pow(count, 2))

except Exception as e:
    print("Error:", e)