# Most Common Data Types In SQL

1. #### INT
   - Whole Numbers.
2. #### DECIMAL (M, N)
   - Decimals, where M & N defines digits before and after decimal point respectively.
3. #### VARCHAR (L)
   - String, of L max length.
4. #### BLOB
   - Binary Large Objects or Multimedia files like Images, Audio, etc.
5. #### DATE
   - Calendar Date, Format - > 'YYYY- MM- DD'.
6. #### TIMESTAMP
   - Date with time, Format - > 'YYYY- MM- DD HH:MM:SS'.

###### **_Some datatypes names may change with respect to DBMS._**

# Operators in SQL

1. ## Comparision Operator

   | Symbol |       Description        | Example |
   | :----: | :----------------------: | ------- |
   |   =    |         Equal to         | a=b     |
   |   <>   |       Not Equal to       | a<>b    |
   |   <    |        Less than         | a<b     |
   |   >    |       Greater than       | a>b     |
   |   >=   | Greater than or Equal to | a>=b    |
   |   <=   |  Less than or Equal to   | a<=b    |

2. ## Logical Operator
   | Symbol  |                         Description                          |
   | :-----: | :----------------------------------------------------------: |
   |   ALL   |    TRUE if all of the subquery values meet the condition     |
   |   AND   |     TRUE if all the conditions separated by AND are TRUE      |
   |   ANY   |    TRUE if any of the subquery values meet the condition     |
   | BETWEEN |    TRUE if the operand is within the range of comparisons    |
   | EXISTS  |       TRUE if the subquery returns one or more records       |
   |   IN    | TRUE if the operand is equal to one of a list of expressions |
   |  LIKE   |            TRUE if the operand matches a pattern             |
   |   NOT   |      Displays a record if the condition(s) is NOT TRUE       |
   |   OR    |    TRUE if any of the conditions separated by OR is TRUE     |
   |  SOME   |    TRUE if any of the subquery values meet the condition     |

# Constraints

- They are used to specify rules for the data in a table.

1. #### NOT NULL :

   - Ensures that a column cannot have a NULL value

     `col_name data_type NOT NULL`

2. #### UNIQUE :

   - Ensures that all values in a column are different

     `col_name data_type UNIQUE`

3. #### PRIMARY KEY :

   - A combination of a NOT NULL and UNIQUE
   - Can only be used once in a table

     `col_name data_type PRIMARY KEY`

     `PRIMARY KEY (col_name);`

4. #### FOREIGN KEY :

   - Prevents actions that would destroy links between tables
   - Primary key for another table which is linked to the table with primary key.

     `FOREIGN KEY (new_table_col) REFERENCES Persons(first_table_primary_key)`

5. #### CHECK :

   - Ensures that the values in a column satisfy a specific condition

     `check (condition)`

6. #### DEFAULT :

   - Sets a default value for a column if no value is specified

     `col_name data_type DEFAULT 'default_value'`

7. #### CREATE INDEX :

   - Used to create and retrieve data from the database very quickly

     `CREATE INDEX index_name ON table_name (col1_name, col2_name);`

     `CREATE UNIQUE INDEX index_name ON table_name (col1_name, col2_name);`

8. #### AUTO_INCREMENT :

   - It allows a unique number to be generated automatically when a new record is inserted into a table.
   - Can also set initial value to start with by using _alter_.

     `alter table student_t0 AUTO_INCREMENT=inital_val;`

# Clauses/Aggregate Queries

- Clauses are built-in functions that help filter and analyze data in a database.

1. #### HAVING :
   - HAVING clause can be used in a GROUP BY clause. It is used to specify a search condition for a group in the database tables.
2. #### WHERE :

   - The WHERE clause in SQL is used to retrieve the specific data from the database that specifies the conditions exactly that are given in the UPDATE, DELETE, etc. statements.

     `SELECT * FROM table_name WHERE condition`

     `DELETE FROM table_name WHERE condition;`

     `UPDATE table_name SET col_name = val WHERE condition`

3. #### ORDER BY :

   - The ORDER BY clause in SQL is used for sorting the records of the database tables.
   - By default Ascending.

     `SELECT * FROM table_name ORDER BY col_name ASC|DESC;`

     `SELECT * FROM table_name ORDER BY col1_name ASC|DESC,col2_name ASC|DESC;`

4. #### GROUP BY :

   - To group the result set of the rows that have the same values in the result set from the database tables, the GROUP BY clause is used.

     `SELECT columns FROM table_name GROUP BY col_name;`

5. #### LIKE :

   - SQL LIKE clause compares a value to similar values using wildcard operators, i.e. percent sign ( % ) and the underscore operator ( \_ ).

     `SELECT columns from table_name where column_name LIKE 'condition';`

6. #### LIMIT :

   - The LIMIT clause is used when you are dealing with large databases. It is used to specify the maximum number of rows to be retrieved from the table.

     `SELECT columns FROM table_name LIMIT value;`

7. #### AS :

   - It is used to rename a column or table with an alias.
   - An alias only exists for the duration of the query.

     `SELECT column_name AS alias FROM table_name;`

     `SELECT column_name FROM table_name AS alias ;`

8. #### MAX :

   - Find the maximum value in a column.

     `SELECT MAX(col_name) FROM table_name;`

9. #### MIN :

   - Find the minimum value in a column.

     `SELECT MIN(col_name) FROM table_name;`

10. #### COUNT :

    - Count the total number of values in the column.

      `SELECT COUNT(col_name) FROM table_name;`

11. #### SUM :

    - Sum of all values in the column.

      `SELECT SUM(col_name) FROM table_name;`

12. #### AVG :

    - Average of all values in the column.

      `SELECT AVG(col_name) FROM table_name;`

13. #### DISTINCT :

    - Return only distinct rows according to respective queries.

      `SELECT DISTINCT * FROM TABLENAME;`

      `SELECT DISTINCT Colummn1, Column2 FROM TABLENAME;`

      `SELECT DISTINCT Colummn1, Column2 FROM TABLENAME WHERE column_name condition;`

14. #### UNION :

    - Combine two or more select queries.

      `SELECT col_name FROM table_name1 UNION SELECT col_name FROM table_name2 ;`

      `SELECT col_name FROM table_name1 UNION ALL SELECT col_name FROM table_name2 ;`

15. #### ON DELETE :

    - ON DELETE constraint is used in MySQL to delete the rows from the child table automatically, when the rows from the parent table are deleted.

    1. ON DELETE CASCADE :

       - The ON DELETE CASCADE clause indicates that when the row in the parent table is deleted, the dependent rows in the child table will also be deleted.

         `Foreign Key(t2_col) references t1(t1_col) ON DELETE SET CASCADE`

    2. ON DELETE SET NULL :

       - The ON DELETE SET NULL clause is a foreign key constraint that sets all records in a column to null if the corresponding record in the parent table is deleted.
       - The child data is not deleted.

         `Foreign Key(t2_col) references t1(t1_col) ON DELETE SET NULL`

# There are 5 Sub- Languages in SQL

1. ## DQL - Data Query Language

- DQL statements perform queries on the data within schema objects.

- The purpose of the DQL Command is to get some schema relation based on the query passed to it.

- Commands :

1. #### SELECT :

   - Return rows according to respective queries.

     `SELECT * FROM TABLENAME;`

     `SELECT Colummn1, Column2 FROM TABLENAME;`

     `SELECT Colummn1, Column2 FROM TABLENAME WHERE column_name condition;`

2. ## DDL - Data Definition Language

- DDL commands that can be used to define the database schema.

- It simply deals with descriptions of the database schema and is used to create and modify the structure of database objects in the database.

- Commands :

1.  #### CREATE :

    - This will create a table in the database with respective column names and attributes.

      `CREATE TABLE table_name (col1_name datatype key(optional));`

      `CREATE TABLE table_name (col1_name datatype,PRIMARY KEY (ol1_name));`

2.  #### DROP :

    - Delete the entire structure or schema and _Rollback_ is impossible. Slower than both _Truncate_ & _Delete_.

      `DROP TABLE table_name;`

3.  #### ALTER :

    - Updates the table's attributes or structure.

      `alter table table_name add column_name datatype;`

      `alter table table_name drop column column_name;`

4.  #### TRUNCATE :

5.  #### COMMENT :

6.  #### RENAME :

- `DESCRIBE table_name;` command can be used to retrieve info about the table.

3.  ## DML - Data Manipulation Language

- DML statements perform queries on the data within database objects or rows in the table.

- The purpose of the DML Command is to perform operations on table records like insert, update, and delete.

- Commands :

1.  #### INSERT :

    - Insert records into the table.

      `INSERT INTO VALUES (col1_val, col2_val);`

      `INSERT INTO (col1_name,col2_name) VALUES (col1_val, col2_val);`

      `INSERT INTO VALUES (col1_val, col2_val), (col1_val2, col2_val2), (col1_val3, col2_val3);`

2.  #### UPDATE :

    - Update records in the table.

      `UPDATE table_name SET col_name = "new_val" WHERE condition;`

      `UPDATE table_name SET col_name = CASE WHEN condition THEN new_val ELSE new_val1 END;`

3.  #### DELETE :

    - Delete records from the table.

      `DELETE FROM table_name;`

      `DELETE FROM table_name WHERE condition;`

4.  ## DCL - Data Control Language
5.  ## TCL - Transaction Control Language

# Joins

- A JOIN clause is used to combine rows from two or more tables, based on a related column between them.

1.  #### JOIN/INNER JOIN

    - This keyword will create the result- set by combining all rows from both the tables where the condition satisfies i.e. the value of the common field will be the same.

      ```
      SELECT
         table1.column1,
         table1.column2,
         table2.column1
      FROM
         table1
         INNER JOIN table2 ON table1.matching_column = table2.matching_column;
      ```

2.  #### LEFT JOIN/LEFT OUTER JOIN/LEFT INCLUSIVE JOIN

    - This join returns all the rows of the table on the left side of the join and matches rows for the table on the right side of the join.

      ```
      SELECT
         table1.column1,
         table1.column2,
         table2.column1
      FROM
         table1
         LEFT JOIN table2 ON table1.matching_column = table2.matching_column;
      ```

3.  #### LEFT EXCLUSIVE JOIN

    - This join returns all the rows of the table on the left side of the join.

      ```
      SELECT
         table1.column1,
         table1.column2,
         table2.column1
      FROM
         table1
         LEFT JOIN table2 ON table1.matching_column = table2.matching_column
      WHERE
         table2.matching_column IS NULL;
      ```

4.  #### RIGHT JOIN/RIGHT OUTER JOIN/RIGHT INCLUSIVE JOIN

    - This join returns all the rows of the table on the right side of the join and matches rows for the table on the left side of the join.

      ```
      SELECT
         table1.column1,
         table1.column2,
         table2.column1
      FROM
         table1
         RIGHT JOIN table2 ON table1.matching_column = table2.matching_column;
      ```

5.  #### RIGHT EXCLUSIVE JOIN

    - This join returns all the rows of the table on the right side of the join.

      ```
      SELECT
         table1.column1,
         table1.column2,
         table2.column1
      FROM
         table1
         LEFT JOIN table2 ON table1.matching_column = table2.matching_column
      WHERE
         table1.matching_column IS NULL;
      ```

6.  #### OUTER JOIN/FULL OUTER JOIN/FULL JOIN/OUTER INCLUSIVE JOIN

    - The result- set will contain all the rows from both tables.

      ```
      SELECT
         table1.column1,
         table1.column2,
         table2.column1
      FROM
         table1 FULL
         JOIN table2 ON table1.matching_column = table2.matching_column;
      ```

7.  #### OUTER EXCLUSIVE JOIN

    - This join returns all the rows of the table on the right side and left side of the join exclusive of matching rows.

      ```
      SELECT
         table1.column1,
         table1.column2,
         table2.column1
      FROM
         table1
         LEFT JOIN table2 ON table1.matching_column = table2.matching_column
      WHERE
         table1.matching_column IS NULL
         OR table2.matching_column IS NULL;
      ```

8.  #### SELF JOIN

    - A self-join in SQL is a type of inner join that joins a table to itself.
    - In a self-join, each row in a table is joined to itself and every other row in that table.

      ```
      SELECT
         column_names
      FROM
         table1 T1,
         table1 T2
      WHERE
         condition;
      ```

9.  #### CROSS JOIN

    - The CROSS JOIN is used to generate a paired combination of each row of the first table with each row of the second table.

      ```
      SELECT
         column_names
      FROM
         table1
         CROSS JOIN table2;
      ```

      ```
      SELECT
         column_names
      FROM
         table1,
         table2;
      ```

10. #### NATURAL JOIN

    - Natural Join joins two tables based on the same attribute name and datatypes.
    - The resulting table will contain all the attributes of both the table but keep only one copy of each common column while Inner Join joins two tables on the basis of the column which is explicitly specified in the ON clause.
    - The resulting table will contain all the attributes from both tables including the common column also.

      ```
      SELECT
         columns
      FROM
         table1
         NATURAL JOIN table2;
      ```

# Nested Queries

- Nested queries are a way to perform more complex queries by embedding one query within another.

- A nested query is a query that appears inside another query, and it helps retrieve data from multiple tables or apply conditions based on the results of another query.

```
SELECT
    t1_cols
from
    t1
WHERE
    condition IN (
        SELECT
            t2_cols
        from
            t2
        WHERE
            condition
    )
```

# Triggers

- A trigger is a stored procedure in a database that automatically invokes whenever a special event in the database occurs.

```
CREATE
     TRIGGER `event_name` BEFORE/AFTER INSERT/UPDATE/DELETE
     ON `database`.`table`
     FOR EACH ROW BEGIN
 	    trigger body
 	    this code is applied to every
 	    inserted/updated/deleted row
     END;
```
