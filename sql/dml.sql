select projects.name as Project, sum(salary) as Total, avg(age) as Avg
from employees
inner join employee_projects as ep on employees.id = ep.employee_id
inner join projects on ep.project_id = projects.id
group by projects.id;
