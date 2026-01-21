import numpy as np

class DataAnalytics:
    def __init__(self, array=None):
        self.array = array

    # Array creation
    @staticmethod
    def create_array(dim):
        if dim == 1:
            elements = list(map(int, input("Enter elements separated by space: ").split()))
            return np.array(elements)
        elif dim == 2:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            elements = list(map(int, input(f"Enter {rows*cols} elements separated by space: ").split()))
            return np.array(elements).reshape(rows, cols)
        elif dim == 3:
            depth = int(input("Enter the depth: "))
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            elements = list(map(int, input(f"Enter {depth*rows*cols} elements separated by space: ").split()))
            return np.array(elements).reshape(depth, rows, cols)

    # Mathematical operations
    def add(self, other):
        return self.array + other

    def subtract(self, other):
        return self.array - other

    def multiply(self, other):
        return self.array * other

    def divide(self, other):
        return self.array / other

    # Combine arrays
    def combine(self, other):
        return np.vstack((self.array, other))

    # Search
    def search(self, value):
        return np.where(self.array == value)

    # Sort
    def sort(self):
        return np.sort(self.array, axis=1)

    # Filter
    def filter_values(self, condition):
        return self.array[condition(self.array)]

    # Aggregates
    def sum(self):
        return np.sum(self.array)

    def mean(self):
        return np.mean(self.array)

    def median(self):
        return np.median(self.array)

    def std(self):
        return np.std(self.array)

    def variance(self):
        return np.var(self.array)

# Menu-driven UI
def main():
    analyzer = None
    while True:
        print("\nWelcome to the NumPy Analyzer!")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            dim = int(input("Select array dimension (1, 2, 3): "))
            arr = DataAnalytics.create_array(dim)
            analyzer = DataAnalytics(arr)
            print("Array created successfully:")
            print(analyzer.array)

        elif choice == 2:
            if analyzer is None:
                print("Create an array first!")
                continue
            print("Choose operation: 1.Add 2.Subtract 3.Multiply 4.Divide")
            op = int(input("Enter choice: "))
            other = np.array(list(map(int, input("Enter same-size array elements: ").split()))).reshape(analyzer.array.shape)
            if op == 1:
                print("Result:", analyzer.add(other))
            elif op == 2:
                print("Result:", analyzer.subtract(other))
            elif op == 3:
                print("Result:", analyzer.multiply(other))
            elif op == 4:
                print("Result:", analyzer.divide(other))

        elif choice == 3:
            if analyzer is None:
                print("Create an array first!")
                continue
            other = np.array(list(map(int, input("Enter another array elements to combine: ").split()))).reshape(analyzer.array.shape)
            print("Combined Array:\n", analyzer.combine(other))

        elif choice == 4:
            if analyzer is None:
                print("Create an array first!")
                continue
            print("Choose: 1.Search 2.Sort 3.Filter")
            sub = int(input())
            if sub == 1:
                val = int(input("Enter value to search: "))
                print("Found at:", analyzer.search(val))
            elif sub == 2:
                print("Sorted Array:\n", analyzer.sort())
            elif sub == 3:
                cond = lambda x: x > int(input("Enter filter threshold: "))
                print("Filtered Array:\n", analyzer.filter_values(cond))

        elif choice == 5:
            if analyzer is None:
                print("Create an array first!")
                continue
            print("Choose: 1.Sum 2.Mean 3.Median 4.Std 5.Variance")
            stat = int(input())
            if stat == 1:
                print("Sum:", analyzer.sum())
            elif stat == 2:
                print("Mean:", analyzer.mean())
            elif stat == 3:
                print("Median:", analyzer.median())
            elif stat == 4:
                print("Standard Deviation:", analyzer.std())
            elif stat == 5:
                print("Variance:", analyzer.variance())

        elif choice == 6:
            print("Thank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
