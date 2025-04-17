class Stack:
    def __init__(self):
        self.stack = []

    
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

        def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty. Cannot perform pop operation.")
        else:
            popped_item = self.stack.pop()
            print(f"{popped_item} popped from stack")

    
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty. Cannot perform peek operation.")
        else:
            print(f"Top element is {self.stack[-1]}")

    
    def is_empty(self):
        return len(self.stack) == 0

    
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack elements:", self.stack)


def menu():
    print("\nStack Menu:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if Stack is Empty")
    print("5. Display Stack")
    print("6. Exit")


def main():
    stack = Stack()
    
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            item = int(input("Enter the number to push: "))
            stack.push(item)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.peek()
        elif choice == 4:
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == 5:
            stack.display()
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
