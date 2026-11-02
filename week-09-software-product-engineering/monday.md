SQL - conected tables to store data more efficiently

CREATE TABLE tbl_members (
m_id   INTEGER PRIMARY KEY,
name TEXT NOT NULL UNIQUE
);

CREATE TABLE tbl_expenses (
  e_id          INTEGER PRIMARY KEY,
  description        TEXT NOT NULL,
  amount INTEGER NOT NULL CHECK (amount >= 0),
  m_id INTEGER NOT NULL REFERENCES tbl_members(m_id)
);

each table has row's and coloumns to store data, 

DATATYPES
INTEGER
TEXT

NOT NULL - Cannot be empty
PRIMARY KEY - Unique indentifier to a record in a table
References - used to link tables together
Check - condition that should pass when data is entered to the table

CRUD Op's
Create: 
INSERT INTO tbl_members (m_id,name) VALUES (1,'Hasthi');
INSERT INTO tbl_expenses (description ,amount, m_id) VALUES ('Netflix Subscription', 10, 1);

Read:
SELECT description, amount FROM tbl_expenses WHERE m_id = 1 ORDER BY name;

Update:
UPDATE tbl_expenses SET amount = 20 WHERE m_id = 1;

Delete:
DELETE FROM tbl_expenses WHERE m_id = 2;

Joining Tables 

SELECT e.description, e.amount, n.name AS TotalPerMember
FROM tbl_expenses e
JOIN tbl_members m ON e.e_id = m.m_id;

Using in python

import sqlite3

db = sqlite3.connect("expenses.db")
db.row_factory = sqlite3.Row

Writing a new nember to the members table
db.execute(
    "INSERT INTO categories (m_id,name) VALUES (?,?)", 
    (1,"Hasthi",)
)

Writing a new expense to the expenses table
db.execute(
    "INSERT INTO tbl_expenses (e_id, description, amount, m_id) VALUES (?, ?, ?,?)", 
    (1,"Notebook", 25000, 1)
)

db.commit()


rows = db.execute("SELECT * FROM categories").fetchall()
for r in rows:
    print(r["id"], r["name"])

db.close()