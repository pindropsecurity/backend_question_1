SELECT
    sub.project_name AS Project,
    SUM(sub.salary) as Total,
    ROUND(AVG(sub.age)) as Avg
FROM (
    SELECT
        employees.id,
        projects.project_name,
        employees.salary,
        employees.age
    FROM
        projects
        JOIN employee_projects ON employee_projects.project_id = projects.project_id
        JOIN employees ON employee_projects.employee_id = employees.id
    GROUP BY projects.project_name, employees.id
    ) sub
GROUP BY sub.project_name
ORDER BY sub.project_name

