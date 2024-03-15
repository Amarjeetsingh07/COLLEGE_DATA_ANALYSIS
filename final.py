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
# Define SQL queries
query_students_per_course = """
select * from enrollments
"""
students_df = """ SELECT c.course_name , s.first_name FROM Courses_ndb c INNER JOIN enrollments e ON c.Course_id = e.course_id INNER JOIN Students_ndb s ON e.student_id = s.Student_id
ORDER BY c.Course_name, s.Student_id;
"""
department_df = """ SELECT d.department_name, c.Course_name FROM Departments_ndb d INNER JOIN Courses_ndb c ON d.department_id = c.department_id
ORDER BY d.department_name, c.course_name;"""
staff_df = """ SELECT c.course_name, s.first_name FROM courses_ndb c JOIN staff_ndb s ON c.department_id = s.department_id;
"""
year_df =""" SELECT semester, year, COUNT(*) AS enrollments_count FROM enrollments GROUP BY semester, year;
"""
# Execute SQL queries and fetch data into pandas DataFrames
students_per_course_df = pd.read_sql(year_df, conn)

# Data Exploration
print(students_per_course_df.head())
print(students_per_course_df.info())
print(students_per_course_df.describe())

# Data Analysis
# Example: Calculate average marks(%ge) of students in each department

# Visualizations
# Example: Bar chart showing enrollment counts by department
plt.figure(figsize=(10, 6))
sns.countplot(x='year', data=students_per_course_df)
plt.title('students enrolled in each course')
plt.xlabel('Department')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Close the database connection
conn.close()
