#Homework 1
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = False

    def mark_complete(self):
        self.status = True

    def __str__(self):
        status = "Complete" if self.status else "Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date.date()}\nStatus: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def list_all_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"Task {i + 1}:\n{task}\n")

    def list_incomplete_tasks(self):
        for i, task in enumerate(self.tasks):
            if not task.status:
                print(f"Task {i + 1}:\n{task}\n")

def main():
    todo = ToDoList()

    while True:
        print("ToDo List Menu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo.add_task(task)
            print("Task added.\n")
        elif choice == '2':
            todo.list_all_tasks()
            index = int(input("Enter task number to mark as complete: ")) - 1
            todo.mark_task_complete(index)
            print("Task marked as complete.\n")
        elif choice == '3':
            todo.list_all_tasks()
        elif choice == '4':
            todo.list_incomplete_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()


#Homework 2
from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.timestamp}\nContent: {self.content}"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        for i, post in enumerate(self.posts):
            print(f"Post {i + 1}:\n{post}\n")

    def display_posts_by_author(self, author):
        for i, post in enumerate(self.posts):
            if post.author == author:
                print(f"Post {i + 1}:\n{post}\n")

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].title = new_title
            self.posts[index].content = new_content
            self.posts[index].timestamp = datetime.now()

    def display_latest_posts(self, count=5):
        sorted_posts = sorted(self.posts, key=lambda x: x.timestamp, reverse=True)
        for i, post in enumerate(sorted_posts[:count]):
            print(f"Latest Post {i + 1}:\n{post}\n")

def main():
    blog = Blog()

    while True:
        print("Blog System Menu:")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added.\n")
        elif choice == '2':
            blog.list_all_posts()
        elif choice == '3':
            author = input("Enter author name: ")
            blog.display_posts_by_author(author)
        elif choice == '4':
            blog.list_all_posts()
            index = int(input("Enter post number to delete: ")) - 1
            blog.delete_post(index)
            print("Post deleted.\n")
        elif choice == '5':
            blog.list_all_posts()
            index = int(input("Enter post number to edit: ")) - 1
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            blog.edit_post(index, new_title, new_content)
            print("Post edited.\n")
        elif choice == '6':
            blog.display_latest_posts()
        elif choice == '7':
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()


#Homework 3
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False

    def __str__(self):
        return f"Account Number: {self.account_number}\nHolder Name: {self.holder_name}\nBalance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def check_balance(self, account_number):
        account = self.get_account(account_number)
        return account.balance if account else None

    def deposit_money(self, account_number, amount):
        account = self.get_account(account_number)
        return account.deposit(amount) if account else False

    def withdraw_money(self, account_number, amount):
        account = self.get_account(account_number)
        return account.withdraw(amount) if account else False

    def transfer_money(self, from_account, to_account, amount):
        acc_from = self.get_account(from_account)
        acc_to = self.get_account(to_account)
        return acc_from.transfer(acc_to, amount) if acc_from and acc_to else False

    def display_account_details(self, account_number):
        account = self.get_account(account_number)
        return str(account) if account else "Account not found."

def main():
    bank = Bank()

    while True:
        print("\nBanking System Menu:")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            acc_no = input("Enter account number: ")
            name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            acc = Account(acc_no, name, balance)
            bank.add_account(acc)
            print("Account added.")
        elif choice == '2':
            acc_no = input("Enter account number: ")
            balance = bank.check_balance(acc_no)
            print(f"Balance: ${balance:.2f}" if balance is not None else "Account not found.")
        elif choice == '3':
            acc_no = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            success = bank.deposit_money(acc_no, amount)
            print("Deposit successful." if success else "Deposit failed.")
        elif choice == '4':
            acc_no = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            success = bank.withdraw_money(acc_no, amount)
            print("Withdrawal successful." if success else "Withdrawal failed or insufficient funds.")
        elif choice == '5':
            from_acc = input("Enter source account number: ")
            to_acc = input("Enter destination account number: ")
            amount = float(input("Enter amount to transfer: "))
            success = bank.transfer_money(from_acc, to_acc, amount)
            print("Transfer successful." if success else "Transfer failed.")
        elif choice == '6':
            acc_no = input("Enter account number: ")
            details = bank.display_account_details(acc_no)
            print(details)
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
