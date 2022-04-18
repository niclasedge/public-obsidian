parent: [[LF05 - Datenbank]]
tags:
aliases: 
Reference:

---
# SQL sample Queries

- [ ]  in deutsch übersetzten
- [ ]  in Mysql syntax umwandeln

**Find Second Highest Salary of Employee?**

- SELECT distinct salary from Employees e1 where 2 = (SELECT count(distinct salary) from Employees e2
- WHERE e1.salary <= e2.salary);
- SELECT * from employees
- where salary not in (SELECT max(salary) from employees)
- fetch first 1 rows only
- SELECT * FROM ( SELECT e.Salary, ROW_NUMBER() OVER (ORDER BY salary DESC) rn FROM Employees e ) WHERE rn = 3;

**How to fetch monthly Salary of Employee if annual salary is given?**

- SELECT first_name, salary, salary*12 as year_sal FROM employees

**Fetch first record FROM Employee table?**

- SELECT * FROM employees fetch first 1 row only;
- SELECT * FROM Employees WHERE Rownum =1;
- **Fetch last record FROM the table?**
- SELECT * FROM Employees WHERE rowid = (SELECT max(rowid) FROM employees);
- **Display first 5 Records FROM Employee table?**
- SELECT * FROM employees fetch first 5 rows only;
- SELECT * FROM employees WHERE rownum <= 5;
- **Display last 5 Records FROM Employee table?**
- SELECT * FROM (SELECT * FROM Employees e order by rowid desc) WHERE rownum <=5 order by rowid;
- **Display Nth Record FROM Employee table?**
- SELECT * FROM ( SELECT a.*, rownum rnum FROM ( SELECT * FROM employees ) a WHERE rownum <= 5 ) WHERE rnum >= 5;

**How to get 3 Highest salaries records FROM Employee table?**

- SELECT salary FROM(SELECT DISTINCT salary FROM employees order by salary desc)WHERE rownum<=3;

**Display Odd rows in Employee table?**

- SELECT * FROM(SELECT rownum as rno,E.* FROM Employees E) WHERE Mod(rno,2)=1;

**Display Even rows in Employee table?**

- SELECT * FROM(SELECT rownum as rno,E.* FROM Employees E) WHERE Mod(rno,2)=0;
- **How to fetch 3rd highest salary using Rank Function?**
- SELECT * FROM (SELECT Dense_Rank() over ( order by salary desc) as Rnk,E.* FROM Employees E) WHERE Rnk=3;

**How Can i create table with same structure of Employee table?**

- CREATE TABLE emp2 as SELECT * FROM employees WHERE 1=2;

**Display first 50% records FROM Employee table?**

- SELECT * FROM employees
- fetch first 50 percent rows only;
- SELECT first_name FROM employees
- WHERE rownum < (SELECT avg(rownum) FROM employees);
- SELECT rownum, e.* FROM employees e WHERE rownum<=(SELECT count(*)/2 FROM employees);

**Display last 50% records FROM Employee table?**

- SELECT * FROM employees
- order by 1 desc
- fetch first 50 percent rows only
- SELECT first_name FROM employees
- WHERE rownum > (SELECT avg(rownum) FROM employees)
- SELECT rownum, E.* FROM Employees E
- minus
- SELECT rownum, E.* FROM Employees E WHERE rownum<=(SELECT count(*)/2) FROM Employees);
- **How Can i create table with same structure with data of Employee table?**
- CREATE TABLE emp2 as SELECT * FROM employees
- **How do i fetch only common records between 2 tables.**
- SELECT * FROM emp e INNER JOIN mgr m on e.employee_id=m.employee_id
- SELECT * FROM Employee;
- Intersect
- SELECT * FROM Employee1;
- **Find duplicate rows in table?**
- SELECT a.* from Employees a where rowid =! (SELECT max(rowid) from Employees b where a.employee_id =b.employee_id);
- **Find Query to get information of Employee WHERE Employee is not assigned to the department**
- SELECT * FROM employees WHERE nvl(department_id,0) NOT IN (SELECT department_id FROM departments)
- --use nvl to show null value, otherwies no data will be found for null
- update employees set department_id = null WHERE employee_id = 104
- **How to get DISTINCT records FROM the table without using DISTINCT keyword.**
- SELECT * FROMN Employee a where rowid = (SELECT max(rowid) from Employee b
- WHERE a.Employee_no=b.Employee_no);
- **SELECT all records FROM Employee table whose name is ‘Amit’ and ‘Pradnya’:**
- SELECT * FROM employees WHERE first_name in ('Steven', 'David‘);
- **SELECT all records FROM Employee table WHERE name NOT IN ‘Amit’ and ‚Pradnya’:**
- SELECT * FROM employees WHERE first_name NOT IN ('Steven', 'David‘);
- **How to write sql query for the below scenario**
- SELECT Substr('ORACLE',Level,1) FROM Dual
- Connect By Level<= Length('ORACLE');

**How to fetch all the records FROM Employee whose JOINing year is 2017?**

- SELECT * FROM employees
- WHERE to_char(hire_date, 'YYYY') = 2005;

**What is SQL Query to find maximum salary of each department?**

- SELECT * FROM departments b full outer JOIN (SELECT department_id, max(salary)
- FROM employees
- GROUP BY department_id ) a
- on b.department_id=a.department_id

**How Do you find all Employees with its managers?(Consider there is manager id also in Employee table)**

- SELECT a.first_name fname, a.employee_id ,b.employee_id manager_id, b.first_name mname FROM employees a JOIN employees b
- on b.employee_id=a.manager_id
- order by 2;
- SELECT fname, count(manager_id)
- FROM(SELECT a.first_name fname, a.employee_id ,b.employee_id manager_id, b.first_name mname FROM employees a JOIN employees b on b.employee_id=a.manager_id
- order by 2) GROUP BY fname
- SELECT e.first_name, e.employee_id,m.first_name FROM Employees e,Employees m WHERE e.Employee_id=m.Manager_id
- order by 2
- **Display the name of employees who have JOINed in 2016 and salary is greater than 10000?**
- SELECT * FROM employees
- WHERE to_char(hire_date, 'YYYY') between 2003 and 2008
- and salary >= 10000;
- **How to display following using query?**
- SELECT lpad('*', ROWNUM,'*') FROM employees WHERE ROWNUM <4;
- SELECT lpad('*', ROWNUM,'*') FROM employees;
- **How to add the email validation using only one query?**
- SELECT Email FROM Employeee
- WHERE NOT REGEXP_LIKE(Email, ‘[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}’, ‘i’);
- **How to display 1 to 100 Numbers with query?**
- SELECT level FROM dual connect by level <=100;
- SELECT rownum FROM employees WHERE rownum <= 100;

**How to remove duplicate rows FROM table?**

- SELECT first_name, count (first_name) FROM employees
- GROUP BY first_name
- HAVING count (first_name)>1
- Order by count (first_name) desc;
- Delete FROM employees WHERE ROWID <>
- (SELECT max(rowid) FROM employees b WHERE first_name=b.first_name);

**How to find count of duplicate rows?**

- SELECT first_name, count (first_name) FROM employees
- GROUP BY first_name
- HAVING count (first_name)>1
- Order by count (first_name) desc;
- Delete FROM employees WHERE ROWID <>
- (SELECT max(rowid) FROM employees b WHERE first_name=b.first_name);

**How to Find the JOINing date of Employee in YYYY-DAY-Date format.**

- SELECT FIRST_NAME, to_char(hire_date,'YYYY') JOINYear , to_char(hire_date,'Mon') Jmon, to_char(hire_date,'dd') Jday FROM EMPLOYEES;