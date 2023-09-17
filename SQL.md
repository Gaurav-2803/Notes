# Most Common Data Types In SQL

1. #### INT
   ##### Whole Numbers.
2. #### DECIMAL (M, N)
   ##### Decimals, where M & N defines digits before and after decimal point respectively.
3. #### VARCHAR (L)
   ##### String, of L max length.
4. #### BLOB
   ##### Binary Large Object or Multimedia files like Images, Audio, etc.
5. #### DATE
   ##### Calendar Date, Format -> 'YYYY-MM-DD'.
6. #### TIMESTAMP
   ##### Date with time, Format -> 'YYYY-MM-DD HH:MM:SS'.

###### **_Some datatypes name may change with respect to DBMS._**

# Constraints

- #### They are used to specify rules for the data in a table.

1. ### NOT NULL :
   - ##### Ensures that a column cannot have a NULL value
     `col_name data_type NOT NULL`
2. ### UNIQUE :
   - ##### Ensures that all values in a column are different
     `col_name data_type UNIQUE`
3. ### PRIMARY KEY :

   - ##### A combination of a NOT NULL and UNIQUE
   - ##### Can only be used once in a table

     `col_name data_type PRIMARY KEY`

     `PRIMARY KEY (col_name);`

4. ### FOREIGN KEY :

   - ##### Prevents actions that would destroy links between tables
   - ##### Primary key for another table which is linked to table with primary key.
     `FOREIGN KEY (new_table_col) REFERENCES Persons(first_table_primary_key)`

5. ### CHECK :
   - ##### Ensures that the values in a column satisfies a specific condition
     `check (condition)`
6. ### DEFAULT :
   - ##### Sets a default value for a column if no value is specified
     `col_name data_type DEFAULT 'default_value'`
7. ### CREATE INDEX :

   - ##### Used to create and retrieve data from the database very quickly

     `CREATE INDEX index_name ON table_name (col1_name, col2_name);`

     `CREATE UNIQUE INDEX index_name ON table_name (col1_name, col2_name);`

8. ### AUTO_INCREMENT :
   - ##### It allows a unique number to be generated automatically when a new record is inserted into a table.
   - ##### Can also set intial value to start with by using _alter_.
     `alter table student_t0 AUTO_INCREMENT=inital_val;`

# There are 5 Sub-Languages in SQL

1. ## DQL - Data Query Language

- ##### DQL statements are used for performing queries on the data within schema objects.

- ##### The purpose of the DQL Command is to get some schema relation based on the query passed to it.

- ### Commands :

  1. #### SELECT : Return rows according respective to queries.

     `SELECT * FROM TABLENAME;`

     `SELECT Colummn1, Column2 FROM TABLENAME;`

     `SELECT Colummn1, Column2 FROM TABLENAME WHERE column_name condition;`

2. ## DDL - Data Definition Language

- ##### DDL commands that can be used to define the database schema.

- ##### It simply deals with descriptions of the database schema and is used to create and modify the structure of database objects in the database.

- ### Commands :

  1.  #### CREATE : This will create table in database with respective Columns names and its attributes.

      `CREATE TABLE table_name (col1_name datatype key(optional));`

      `CREATE TABLE table_name (col1_name datatype,PRIMARY KEY (ol1_name));`

  2.  #### DROP : Delete the entire structure or schema and _Rollback_ is not possible. Slower than both _Truncate_ & _Delete_.

      `DROP TABLE table_name;`

  3.  #### ALTER : Updates the tables attributes or stucture.

      `alter table table_name add column_name datatype;`

      `alter table table_name drop column column_name;`

  4.  #### TRUNCATE :

  5.  #### COMMENT :

  6.  #### RENAME :

  - `DESCRIBE table_name;` command can be used to retrieve info about table.

3.  ## DCL - Data Control Language

4.  ## DML - Data Manipulation Language

- ##### DML statements are used for performing queries on the data within database objects or rows in table.

- ##### The purpose of the DML Command is to perform operation on table records like insert, update and delete.

- ### Commands :

  1. #### INSERT : Insert records into table.

     `INSERT INTO VALUES (col1_val, col2_val);`

     `INSERT INTO (col1_name,col2_name) VALUES (col1_val, col2_val);`

     `INSERT INTO VALUES (col1_val, col2_val), (col1_val2, col2_val2), (col1_val3, col2_val3);`

  2. #### UPDATE : Update records in table.
  3. #### DELETE : Delete records from table.

5.  ## TCL - Transaction Control Language
