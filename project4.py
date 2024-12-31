import statistics

print("Welcome to the data analyzer and transformer program")

def input_data():
    try:
        data = list(map(int, input("Enter the list of integers: ").split()))
        return data
    except ValueError:
        print("Invalid input! Please enter integers only.")
        return input_data()

def display_summarydata(data):
    print("Summary data:")
    print(f"Count: {len(data)}")
    print(f"Sum: {sum(data)}")
    print(f"Average: {statistics.mean(data) if data else 'N/A'}")
    print(f"Median: {statistics.median(data) if data else 'N/A'}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def filter_data(data, threshold):
    return list(filter(lambda x: x >= threshold, data))

def sort_data(data):
    return sorted(data)

def dataset_statistics(data):
    return {
        "count": len(data),
        "sum": sum(data),
        "mean": statistics.mean(data) if data else None,
        "median": statistics.median(data) if data else None,
        "max": max(data) if data else None,
        "min": min(data) if data else None,
    }

def main():
    dataset = []  # Initialize dataset
    while True:
        print("\nMain menu:")
        print("1. Input data")
        print("2. Display data summary")
        print("3. Calculate factorial")
        print("4. Filter data")
        print("5. Sort data")
        print("6. Dataset statistics")
        print("7. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            dataset = input_data()
        elif choice == 2:
            if dataset:
                display_summarydata(dataset)
            else:
                print("Dataset is empty. Please input data first.")
        elif choice == 3:
            try:
                num = int(input("Enter a number to calculate the factorial: "))
                print(f"Factorial of {num} is: {factorial(num)}")
            except ValueError:
                print("Invalid input! Please enter an integer.")
        elif choice == 4:
            if dataset:
                try:
                    threshold = int(input("Enter the threshold: "))
                    filtered_data = filter_data(dataset, threshold)
                    print(f"Filtered data: {filtered_data}")
                except ValueError:
                    print("Invalid threshold! Please enter an integer.")
            else:
                print("Dataset is empty. Please input data first.")
        elif choice == 5:
            if dataset:
                sorted_data = sort_data(dataset)
                print(f"Sorted data: {sorted_data}")
            else:
                print("Dataset is empty. Please input data first.")
        elif choice == 6:
            if dataset:
                stats = dataset_statistics(dataset)
                print("Dataset Statistics:")
                for key, value in stats.items():
                    print(f"{key.capitalize()}: {value}")
            else:
                print("Dataset is empty. Please input data first.")
        elif choice == 7:
            print("Exiting the program!")
            break
        else:
            print("Invalid choice! Please select a valid option from 1 to 7.")

if __name__ == "__main__":
    main()
