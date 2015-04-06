/*Query 1: select project names ordered by project name*/;

select
project_name
from
projects
order by
project_name;

/*Query 2: select sum of salaries of employees on each project*/;

select sum(salary) total_salaries, project_name
from projects p, employee_projects ep, employees e
where ep.project_id=p.project_id
and e.id=ep.employee_id
group by p.project_id
order by project_name;

/*Query 3: Select average age of employees across projects*/;

select avg(age) average_age, project_name
from projects p, employee_projects ep, employees e
where ep.project_id=p.project_id
and e.id=ep.employee_id
group by p.project_id
order by project_name;

/*Sorry about the shorthand joins, and all lowercase, I really am that lazy :)
Also, I didn't see any point in including a count() clause since it will group together fine with only the sum() or avg().
As far as indexes, pretty much anything with a _id is good practice, and should be an actual foreign key.
Also, since we're sorting on project_name it can't hurt, but it really depends on how many projects there are.*/;