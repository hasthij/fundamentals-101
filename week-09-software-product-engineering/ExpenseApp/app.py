import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

db = sqlite3.connect("expenses.db", check_same_thread=False)
db.row_factory = sqlite3.Row

db.execute("CREATE TABLE IF NOT EXISTS tbl_members (m_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE)")
db.execute("""CREATE TABLE IF NOT EXISTS tbl_expenses (
    e_id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    amount INTEGER NOT NULL CHECK (amount >= 0),
    m_id INTEGER NOT NULL REFERENCES tbl_members(m_id))""")
db.commit()


@app.route('/')
def home():
    totals = db.execute(
        "SELECT m.name, SUM(e.amount) AS total FROM tbl_expenses e "
        "JOIN tbl_members m ON e.m_id = m.m_id GROUP BY m.m_id").fetchall()
    return render_template('dashboard.html', totals=totals)


@app.route('/expenses')
def expenses():
    members = db.execute("SELECT * FROM tbl_members").fetchall()
    return render_template('expenses.html', members=members)


@app.route('/addMember', methods=['POST'])
def addMember():
    db.execute("INSERT INTO tbl_members (name) VALUES (?)", (request.form['name'],))
    db.commit()
    return expenses()


@app.route('/addExpense', methods=['POST'])
def addExpense():
    db.execute(
        "INSERT INTO tbl_expenses (description, amount, m_id) VALUES (?, ?, ?)",
        (request.form['description'], request.form['amount'], request.form['m_id']))
    db.commit()
    return expenses()


if __name__ == '__main__':
    app.run(debug=True)