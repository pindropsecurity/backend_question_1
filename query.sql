SELECT
	p.project_name AS 'Project',
    FORMAT(SUM(em.salary), 2) AS 'Total',
    FORMAT(AVG(em.age), 0) AS 'Avg'
FROM projects AS p
LEFT JOIN employee_projects AS ep
	ON p.project_id = ep.project_id
LEFT JOIN employees AS em
	ON em.employee_id = ep.employee_id
GROUP BY p.project_id;

/*
Example Output:
    ============================
	| Project   | Total  | Avg |
	============================
    | pindrop1	| 120.00 | 25  |
    ------------|--------|-----|
	| pindrop2	| 100.00 | 29  |
    ============================

Suggested indices:

	employees:
		employee_id : Primary Key

    project:
		project_id : Primary Key

    employee_projects:
		project_id, employee_id : Both fields together as a candidate primary key
*/