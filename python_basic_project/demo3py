def manage_marks():
    marks = []

    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter marks for subject{i+1}:"))
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input! Enter numbers only.")

    print("Marks:", marks)
    print("Average:", sum(marks) / len(marks))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))

    marks.sort(reverse=True)
    print("Sorted (Descending):", marks)


manage_marks()