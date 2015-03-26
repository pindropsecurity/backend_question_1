interview_question_1
====================

Interview Question Q1 2015

Submissions
---------------

1. Publicly: Fork this repo and send us a pull request.
2. Privately: Send us a tar.gz of your solution **including your .git folder** so we can see your commit history.


## Questions 

####Python Programming
You are given a tree representing a basic mathematical expression, where:
- The number of children extending from any node is greater than or equal to 2.
- Each node could either be a mathematical operator or a real number. 
- Each of the leaf nodes should be (no promises :-)) a real number - Hint : Handle error here....
- The mathematical operators come from the set (-, +, /, *)
- If a node is a mathematical operator, the operation should be evaluated left-to-right:
 - So, if you have a subtraction node with 1, 2 and 3 you would evaluate as 1 - 2 - 3 = -4. Write a method that calculates the value of such a tree.
Write an python program that calculates the value of the tree. Assume your code is part of a production grade library, so exceptional cases should be handled accordingly.

**NOTE**
- Your implementation should use *only* Python standard library modules. Do not `import some_graph_libary`. Write your own tree implementation and traversal methods.

Some tips:
- Classes, inheritance and encapsulation are your friends
- Code readability >> subtle performance gains
- Unit tests


---
####MySQL
Given the following tables :

|employees|
|---------|
| name    |
| id      |
| salary  |
| age     |

projects|
---------
| project_id   |
| project_name |

employee_projects |
------------------
| employee_id |
| project_id  |
| time_spent  |

Write a select statement returning the following data ordered by project name:
* project name
* sum of all salaries of all employees on the project
* average age of all employees on the project

_Bonus Points : What indexes would you add to make your query go faster._

Example result set:

Project       | Total  | Avg |
--------------|--------|----------
| Mad Cash App  | 500000 | 33  |
| Big Money App | 300000 | 35  |
