class Stack:
    def _int_(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
        print(f"{item} pushed into stack")
    
    def pop(self):
        if len(self.stack) == 0:
            print("stack is empty")
        else:
            popped_item = self.stack.pop()
            print(f"{popped_item} popped from stack")

    def peel(self):
        if len(self.stack) == 0:
            print("stack is empty")

        else:
            print(f"Top element is {self.stack[-1]}")

    def is_empty(self):
        return len(self.stack) == 0:
    
    def display(self):
        if len(self.stack) == 0:
            print("stack is empty")
        else:
            print("stack elements" , self.stack)

    def menu():
        print("\nstack  Menu:")
        print("1. Push:")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if stack is empty")
        print("5. Display Stack")
        print("6. Exit")

        def main():
            stack = Stack()
        while True:
            menu()
            choice = int(input("Enter the number of your choice:"))

            if choice == 1:
                item = int(input("Enter the number to push:"))
                Stack.push(item)

            elif choice == 2:
                Stack.pop()
            elif choice == 3:
                Stack.peel
            elif choice == 4:
                if Stack.is_empty():
                    print("stack is empty")
                else:
                    print("stack is not empty")
            elif choice == 5:
                Stack.display()
            elif choice == 6:
                print('Existing Programn')
                break
            else:
                print("Invalid choice")

                
            