SELECT projects.project_name as Project, SUM(employees.salary) as Total, AVG(employees.age) as "Avg"
FROM employees
JOIN employee_projects on employees.id = employee_projects.employee_id
JOIN projects on projects.project_id = employee_projects.project_id
GROUP BY projects.project_id;

/* I would index employees.id, employee_projects.employee_id, employee_projects.project_id,
and project.project_id
*/