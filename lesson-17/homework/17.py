# Homework 1:
import pandas as pd
import numpy as np

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
        'Age': [25, 30, 35, 40], 
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# 1. Rename column names using function
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

# 2. Print the first 3 rows of the DataFrame
print("First 3 rows of the DataFrame:")
print(df.head(3))

# 3. Find the mean age of the individuals
mean_age = df['age'].mean()
print("\nMean age of the individuals:", mean_age)

# 4. Select and print only the 'first_name' and 'City' columns
print("\nSelected columns (first_name and City):")
print(df[['first_name', 'City']])

# 5. Add a new column 'Salary' with random salary values
np.random.seed(42)  # Set seed for reproducibility
df['Salary'] = np.random.randint(50000, 100000, size=len(df))

# 6. Display summary statistics of the DataFrame
print("\nSummary statistics of the DataFrame:")
print(df.describe())


# Homework 2:
import pandas as pd

# 1. Create the DataFrame 'sales_and_expenses'
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(data)

# 2. Calculate and display the maximum sales and expenses
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print(f"Maximum Sales: {max_sales}")
print(f"Maximum Expenses: {max_expenses}")

# 3. Calculate and display the minimum sales and expenses
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print(f"Minimum Sales: {min_sales}")
print(f"Minimum Expenses: {min_expenses}")

# 4. Calculate and display the average sales and expenses
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print(f"Average Sales: {avg_sales}")
print(f"Average Expenses: {avg_expenses}")


# Homework 3:
import pandas as pd

# 1. Create the DataFrame 'expenses'
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(data)
expenses = expenses.set_index('Category')

# 2. Calculate and display the maximum expense for each category
max_expenses = expenses.max(axis=1)
print("Maximum Expense for Each Category:")
print(max_expenses)

# 3. Calculate and display the minimum expense for each category
min_expenses = expenses.min(axis=1)
print("\nMinimum Expense for Each Category:")
print(min_expenses)

# 4. Calculate and display the average expense for each category
avg_expenses = expenses.mean(axis=1)
print("\nAverage Expense for Each Category:")
print(avg_expenses)
