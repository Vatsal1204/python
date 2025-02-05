import re

def main():
    print("Welcome to the Pattern Extractor and Command-Line Utility")
    print("----------------------------------------------------------")
    while True:
        print("\nChoose an operation:")
        print("1. Extract email addresses from text")
        print("2. Find all phone numbers matching a specific pattern")
        print("3. Count occurrences of a specific word in text")
        print("4. Replace a pattern in the text with another string")
        print("5. Load text from a file")
        print("6. Save results to a new file")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter the text to process: ")
            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
            print("\nExtracting email addresses...")
            if emails:
                print("Found email addresses:")
                for idx, email in enumerate(emails, 1):
                    print(f"{idx}. {email}")
            else:
                print("No email addresses found.")

        elif choice == "2":
            text = input("Enter the text to process: ")
            pattern = input("Enter the phone number pattern (e.g., \\d{3}-\\d{3}-\\d{4}): ")
            phone_numbers = re.findall(pattern, text)
            print("\nExtracting phone numbers...")
            if phone_numbers:
                print("Found phone numbers:")
                for idx, number in enumerate(phone_numbers, 1):
                    print(f"{idx}. {number}")
            else:
                print("No phone numbers found.")

        elif choice == "3":
            text = input("Enter the text to process: ")
            word = input("Enter the word to count: ")
            count = text.count(word)
            print(f"\nCounting occurrences of '{word}'...")
            print(f"The word '{word}' appears {count} times.")

        elif choice == "4":
            text = input("Enter the text to process: ")
            pattern = input("Enter the pattern to replace: ")
            replacement = input("Enter the replacement string: ")
            updated_text = re.sub(pattern, replacement, text)
            print("\nReplacing pattern...")
            print("Updated text:")
            print(updated_text)

        elif choice == "5":
            file_path = input("Enter the file path: ")
            try:
                with open(file_path, 'r') as file:
                    text = file.read()
                    print("Loaded text:")
                    print(text)
            except FileNotFoundError:
                print("File not found. Please check the file path.")

        elif choice == "6":
            text_to_save = input("Enter the text to save: ")
            file_path = input("Enter the file path to save: ")
            with open(file_path, 'w') as file:
                file.write(text_to_save)
            print("Text saved successfully.")

        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()