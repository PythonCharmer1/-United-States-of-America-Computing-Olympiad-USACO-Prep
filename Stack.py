# By Yusuf Ali
# This program is a Basic execution of the Stack Data Type
# A Stack is a Last In First Out data type
# This program uses a basic list as an Stack Data Type


Stack = []

def Push(input):
    Stack.append(input)

def Peak():
    return Stack[-1]

def Pop():
    remove = Stack[-1]
    Stack.remove(remove)


Push(10)
Push(100)
Push(1000)
Push(2000)
Push(3000)
Push(4000)
Push(5000)
Pop()
print(Peak())
