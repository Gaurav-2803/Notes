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

# There are 5 Sub-Languages in SQL

1. ## DQL - Data Query Language

- ##### DQL statements are used for performing queries on the data within schema objects.

- ##### The purpose of the DQL Command is to get some schema relation based on the query passed to it.

- ### Commands :

  1. #### SELECT : Return rows according respective to queries.

     `SELECT * FROM TABLENAME;s`

     `SELECT Colummn1, Column2 FROM TABLENAME;`

     `SELECT Colummn1, Column2 FROM TABLENAME WHERE column_name condition;`

2. ## DDL - Data Definition Language

- ##### DQL commands that can be used to define the database schema.

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

5.  ## TCL - Transaction Control Language
