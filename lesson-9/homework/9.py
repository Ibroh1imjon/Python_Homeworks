# 1. Circle Class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


# 2. Person Class
from datetime import datetime
class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    def get_age(self):
        today = datetime.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))


# 3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"


# 4. Shape and Subclasses
import math
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4 * self.side


# 5. Binary Search Tree Class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(root, key):
            if not root:
                return Node(key)
            if key < root.key:
                root.left = _insert(root.left, key)
            else:
                root.right = _insert(root.right, key)
            return root
        self.root = _insert(self.root, key)

    def search(self, key):
        def _search(root, key):
            if not root:
                return False
            if key == root.key:
                return True
            elif key < root.key:
                return _search(root.left, key)
            else:
                return _search(root.right, key)
        return _search(self.root, key)


# 6. Stack Data Structure
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None


# 7. Linked List Data Structure
class NodeLL:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
        print("None")

    def insert(self, data):
        new_node = NodeLL(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if curr:
            if prev:
                prev.next = curr.next
            else:
                self.head = curr.next


# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())


# 9. Stack with Display
class StackWithDisplay:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

    def display(self):
        print(self.items)


# 10. Queue Data Structure
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)


# 11. Bank Class
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"{self.name}'s balance: {self.balance}")
