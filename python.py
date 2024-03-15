import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the database
#conn = pyodbc.connect('DRIVER={YourDriver};SERVER=YourServer;DATABASE=YourDatabase;UID=YourUsername;PWD=YourPassword')
driver_name ='ODBC Driver 17 for SQL Server'
server_name = 'LAPTOP-TCB6AV9G\SQLEXPRESS'
Database_name = 'college_database_analyse'
connection_string=f"""DRIVER={{{driver_name}}};
SERVER={server_name};
Database={Database_name};
trusted_connection=yes;
encrypt=no"""
conn = pyodbc.connect(connection_string)
# SQL query
sql_query = "SELECT * FROM Grades_ndb"
sql_query2 = "SELECT * FROM Students_ndb"

# Execute query and fetch data into a pandas DataFrame
grades = pd.read_sql(sql_query, conn)
Students = pd.read_sql(sql_query2, conn)
# Assuming you have a DataFrame named 'grades' containing student grades with columns student_id, marks, and department_id
print (grades)
print (Students)
# Merge grades with students to get department information
merged_data = pd.merge(grades, Students, on='student_id', how='inner')

# Calculate average marks (%) by department
average_marks_by_department = merged_data.groupby('student_id')['marks'].mean()

print(average_marks_by_department)

print(average_marks_by_department.head())
print(average_marks_by_department.info())
print(average_marks_by_department.describe())

plt.figure(figsize=(10, 6))
sns.countplot(x='session', data=average_marks_by_department)
plt.title('students enrolled in each course')
plt.xlabel('Department')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

conn.close()