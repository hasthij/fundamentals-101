from flask import Flask,render_template,request

app = Flask(__name__)

expenses_list = []
members_list = []

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/expenses')
def expenses():
    return render_template('expenses.html')

@app.route('/addMember', methods=['POST'])
def addMember():
    name = request.form['name']
    members_list.append(name)
    #database save can go here
    print(members_list)
    return render_template('expenses.html')


@app.route('/addExpense', methods=['POST'])
def addExpense():
    description = request.form['description']
    amount = request.form['amount']
    expenses_list.append({'description': description, 'amount': amount})
    #database save can go here
    print(expenses_list)
    render_template('expenses.html')