-- Crete Employee Table
create table
    employee (
        emp_id int Primary Key,
        first_name varchar(20),
        last_name VARCHAR(20),
        birth_date DATE,
        sex CHAR(1),
        salary INT,
        super_id INT,
        branch_id INT
    );

-- Create Branch Table
create table
    branch(
        branch_id int primary key,
        branch_name varchar(10),
        mgr_id int,
        mgr_start_date date,
        Foreign Key(mgr_id) references employee(emp_id) on delete
        set
            null
    );

-- Add foreign key to branch id (Employee -> Branch)
alter table
    employee
add
    foreign key(branch_id) references branch(branch_id) on delete
set
    null;

-- Add foreign key to super_id (Employee -> Employee)
alter table
    employee
add
    foreign key(super_id) references employee(emp_id) on delete
set
    null;

-- Create Client Table
create table
    client(
        client_id int primary key,
        client_name varchar(20),
        branch_id int,
        foreign key(branch_id) references branch(branch_id) on delete
        set
            null
    );

-- Create work_with Table
create table
    work_with(
        emp_id int,
        client_id int,
        total_sales int,
        primary key(emp_id, client_id),
        foreign key(emp_id) references employee(emp_id) on delete cascade,
        foreign key(client_id) references client(client_id) on delete cascade
    );

-- Create Branch Supplier Table
create table
    branch_supplier(
        branch_id int,
        supplier_name varchar(20),
        supply_type varchar(20),
        primary key(branch_id, supplier_name),
        foreign key(branch_id) references branch(branch_id) on delete cascade
    );

/* Insert Records */
-- Table Employee
INSERT into
    employee
values
    (
        100,
        'David',
        'Wallace',
        '1967-11-17',
        'M',
        250000,
        Null,
        NUll
    );

update
    employee
set
    branch_id = 1
where
    emp_id = 100;

INSERT into
    employee
values
    (
        101,
        'Jan',
        'Levinson',
        '1961-05-11',
        'F',
        110000,
        100,
        1
    );

INSERT into
    employee
values
    (
        102,
        'Michael',
        'Scott',
        '1964-03-15',
        'M',
        75000,
        100,
        null
    );

update
    employee
set
    branch_id = 2
where
    emp_id = 102;

insert into
    employee
values
    (
        103,
        'Angela',
        'Martin',
        '1971-06-25',
        'F',
        63000,
        102,
        2
    ),
    (
        104,
        'Kelly',
        'Kapoor',
        '1980-02-05',
        'F',
        55000,
        102,
        2
    ),
    (
        105,
        'Stanley',
        'Hudson',
        '1958-02-19',
        'M',
        69000,
        102,
        2
    );

insert into
    employee
values
    (
        106,
        'Josh',
        'Porter',
        '1969-09-05',
        'M',
        78000,
        100,
        null
    );

update
    employee
set
    branch_id = 3
where
    emp_id = 106;

insert into
    employee
values
    (
        107,
        'Andy',
        'Bernard',
        '1973-07-22',
        'M',
        65000,
        106,
        3
    ),
    (108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);

-- Table Branch
INSERT INTO
    branch
VALUES
    (1, 'Corporate', 100, '2006-02-09');

INSERT INTO
    branch
VALUES
    (2, 'Scranton', 102, '1992-04-06');

INSERT INTO
    branch
VALUES
    (3, 'Stamford', 106, '1998-02-13');

-- Table Client
INSERT INTO
    client
VALUES
    (400, 'Dunmore Highschool', 2),
    (401, 'Lackawana Country', 2),
    (402, 'FedEx', 3),
    (403, 'John Daly Law, LLC', 3),
    (404, 'Scranton Whitepages', 2),
    (405, 'Times Newspaper', 3),
    (406, 'FedEx', 2);

-- Table Work_With
INSERT INTO
    work_with
VALUES
(105, 400, 55000),
    (102, 401, 267000),
    (108, 402, 22500),
    (107, 403, 5000),
    (108, 403, 12000),
    (105, 404, 33000),
    (107, 405, 26000),
    (102, 406, 15000),
    (105, 406, 130000);

-- Table Branch Supplier
INSERT INTO
    branch_supplier
VALUES
    (2, 'Hammer Mill', 'Paper'),
    (2, 'Uni-ball', 'Writing Utensils'),
    (3, 'Patriot Paper', 'Paper'),
    (2, 'J.T. Forms & Labels', 'Custom Forms'),
    (3, 'Uni-ball', 'Writing Utensils'),
    (3, 'Hammer Mill', 'Paper'),
    (3, 'Stamford Lables', 'Custom Forms');

/* Display Results */
-- Employee
SELECT
    *
FROM
    employee;

-- Branch
SELECT
    *
FROM
    branch;

-- Client
SELECT
    *
FROM
    client;

-- Work With
SELECT
    *
FROM
    work_with;

-- Branch Supplier
SELECT
    *
FROM
    branch_supplier;

/* Describe */
describe
    employee;

describe
    branch;

describe
    client;

describe
    work_with;

describe
    branch_supplier;
