from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.120.52.101;DATABASE=Patio;UID=it;PWD=it')
cursor = cnxn.cursor()


@app.route('/')
def home():
    return render_template('index.html', title='main')


@app.route('/order/')
def order():
    cursor.execute('SELECT * '
                   'FROM LV_Order '
                   'WHERE ord_InputDate > GETDATE()-1'
                   'ORDER BY ord_InputDate DESC')
    return render_template('order.html', title='database', items=cursor.fetchall())


@app.route('/order/<ord_code>')
def order_detail(ord_code):
    cursor.execute(
                   'SELECT * '
                   'FROM LV_OrderItem INNER JOIN '
                   'LV_ProductLang ON LV_OrderItem.ori_ProductID = LV_ProductLang.prdl_ProductID '
                        'AND LV_ProductLang.prdl_LanguageID = 4 '
                   'WHERE ori_OrderID = ' + ord_code)
    return render_template('order_detail.html', title='order', items=cursor.fetchall())


if __name__ == '__main__':
    app.run(debug=True)
