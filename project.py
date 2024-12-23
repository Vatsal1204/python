print("Welcome to the Pattern Generator and Number Analyser")
print("Select an option:")
print("1. For Pattern")
print("2. For Number")
print("3. To Exit")
choice = input("Select an option: ")

if choice == "1":
    print(f"Choose a pattern type:")
    print(f"1. For Right-Angled Triangle")
    print(f"2. For Pyramid")
    print(f"3. For Diamond")
    pattern_type = input("Select a pattern option: ")

    if pattern_type == "1":
        rows = int(input("Enter the number of rows: "))
        for i in range(1, rows + 1):
            print("*" * i)

    elif pattern_type == "2":
        rows = int(input("Enter the number of rows: "))
        for i in range(1, rows + 1):
            spaces = ' ' * (rows - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)

    elif pattern_type == "3":
        rows = int(input("Enter the number of rows: "))
        
        for i in range(1, rows + 1):
            spaces = ' ' * (rows - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)
        
        for i in range(rows - 1, 0, -1):
            spaces = ' ' * (rows - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)

    else:
        print(f"Invalid pattern option!")

elif choice == "2":
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    if start > end:
        print("Invalid range")
    else:
        numbers = list(range(start, end + 1))
        print(f"Numbers in range: {numbers}")
        print(f"Sum: {sum(numbers)}")
        print(f"Average: {sum(numbers) / len(numbers):.2f}")
        print(f"Minimum: {min(numbers)}")
        print(f"Maximum: {max(numbers)}")
        print(f"Even Numbers: {[num for num in numbers if num % 2 == 0]}")
        print(f"Odd Numbers: {[num for num in numbers if num % 2 != 0]}")

elif choice == "3":
    print("Exiting the program. Goodbye!")

else:
    print("Invalid choice!")
