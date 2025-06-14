# DataFrame 1: Student Grades
import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Exercise 1: Calculate average grade for each student
df1["Average"] = df1[["Math", "English", "Science"]].mean(axis=1)

# Exercise 2: Find student with highest average grade
top_student = df1.loc[df1["Average"].idxmax()]
print("Student with highest average grade:")
print(top_student)

# Exercise 3: Add 'Total' column
df1["Total"] = df1[["Math", "English", "Science"]].sum(axis=1)

# Exercise 4: Bar chart of average grades per subject
subject_averages = df1[["Math", "English", "Science"]].mean()
subject_averages.plot(kind='bar', title='Average Grades per Subject', ylabel='Average Grade', color=['skyblue', 'salmon', 'lightgreen'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# DataFrame 2: Sales Data
import pandas as pd
import matplotlib.pyplot as plt

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# Exercise 1: Total sales for each product
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Total Sales for Each Product:")
print(total_sales)

# Exercise 2: Date with highest total sales
df2["Total_Sales"] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_sales_date = df2.loc[df2["Total_Sales"].idxmax(), "Date"]
print(f"\nDate with highest total sales: {max_sales_date}")

# Exercise 3: Percentage change in sales from previous day
pct_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
pct_change.columns = ['Product_A_Change(%)', 'Product_B_Change(%)', 'Product_C_Change(%)']
print("\nPercentage Change in Sales from Previous Day:")
print(pct_change.round(2))

# Exercise 4: Line chart of sales trends
plt.figure(figsize=(10, 6))
plt.plot(df2['Date'], df2['Product_A'], marker='o', label='Product A')
plt.plot(df2['Date'], df2['Product_B'], marker='s', label='Product B')
plt.plot(df2['Date'], df2['Product_C'], marker='^', label='Product C')
plt.title("Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# DataFrame 3: Employee Information
import pandas as pd
import matplotlib.pyplot as plt

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Exercise 1: Average salary for each department
avg_salary = df3.groupby('Department')['Salary'].mean()
print("Average Salary by Department:")
print(avg_salary)

# Exercise 2: Employee with most experience
most_exp_employee = df3.loc[df3['Experience (Years)'].idxmax()]
print("\nEmployee with Most Experience:")
print(most_exp_employee)

# Exercise 3: Salary Increase (%) from minimum salary
min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary) * 100

# Exercise 4: Bar chart of employee distribution by department
dept_counts = df3['Department'].value_counts()
dept_counts.plot(kind='bar', color='cornflowerblue', title='Employee Distribution by Department', ylabel='Number of Employees')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# DataFrame 4: Customer Orders
import pandas as pd
import matplotlib.pyplot as plt

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# Exercise 1: Total revenue from all orders
total_revenue = df4['Total_Price'].sum()
print(f"Total Revenue from all orders: ${total_revenue}")

# Exercise 2: Most ordered product (by quantity)
most_ordered_product = df4.groupby('Product')['Quantity'].sum().idxmax()
print(f"Most ordered product: Product {most_ordered_product}")

# Exercise 3: Average quantity of products ordered
avg_quantity = df4['Quantity'].mean()
print(f"Average quantity ordered per order: {avg_quantity:.2f}")

# Exercise 4: Pie chart of sales distribution by product (based on total price)
sales_by_product = df4.groupby('Product')['Total_Price'].sum()
sales_by_product.plot(kind='pie', autopct='%1.1f%%', startangle=90, legend=False, 
                      title='Sales Distribution by Product', colors=['#66b3ff','#99ff99','#ffcc99'])
plt.ylabel('')
plt.tight_layout()
plt.show()
