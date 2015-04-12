select project_name as Project, avg(age) as Avg, sum(time_spent) as Total
from employee_projects
	join projects
		on employee_projects.project_id = projects.project_id
	join employees
		on employees.id = employee_projects.employee_id
group by project_name;