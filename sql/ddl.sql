create table employees(
  id int not null auto_increment primary key,
  name varchar(50),
  salary int,
  age int
);

create table projects(
  id int not null auto_increment primary key,
  name varchar(50)
);

create table employee_projects(
  employee_id int,
  project_id int,
  constraint emp_proj_pk primary key (employee_id, project_id),
  constraint fk_emp foreign key (employee_id) references employees (id),
  constraint fk_proj foreign key (project_id) references projects (id)
);


insert into employees (name, salary, age) values
('user1', 85000, 30),
('user2', 95000, 29),
('user3', 100000, 25),
('user4', 95000, 23),
('user5', 95000, 21);

insert into projects (name) values
('projectX'),
('projectY'),
('projectZ');

insert into employee_projects values
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 3),
(3, 1),
(4, 1),
(4, 2),
(5, 1),
(5, 3);
