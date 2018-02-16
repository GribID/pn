from flask import Flask, render_template, request
import pyodbc
import sql

app = Flask(__name__)

#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.120.52.101;DATABASE=Patio;UID=it;PWD=it')
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.120.52.101;DATABASE=Patio;UID=it;PWD=it')
cursor = cnxn.cursor()


@app.route('/')
def home():
    return render_template('index.html', title='main')


@app.route('/order/')
def order():
    cursor.execute(sql.order)
    return render_template('order.html', title='database', items=cursor.fetchall())


@app.route('/order/<ord_code>')
def order_detail(ord_code):
    cursor.execute(sql.order_item + ord_code)
    return render_template('order_detail.html', title='order', items=cursor.fetchall())


@app.route('/task/', methods=['GET', 'POST'])
def task():
    if request.method == 'POST':
         return str(request.form['mindate'])

    d = cursor.execute(sql.dep)
    return render_template('task.html', title='task', items=d.fetchall())


if __name__ == '__main__':
    app.run(debug=True)
