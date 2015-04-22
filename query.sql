
select  p.project_name
        sum(e.salary),
		average(e.age)
from    
        employee_projects
		inner join projects p on p.project_id = employee_projects.project_id
		inner join employees e on e.id = employee_projects.employee_id 
group by 
        p.project_name
order by
        p.project_name
       
