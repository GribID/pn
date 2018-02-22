from flask import Flask, render_template, request
import sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title='main')


@app.route('/order/')
def order():
    sn = sql.zz(sql.order)
    return render_template('order.html', title='database', items=sn.fetchall())


@app.route('/order/<ord_code>')
def order_detail(ord_code):
    sn = sql.zz(sql.order_item + ord_code)
    return render_template('order_detail.html', title='order', items=sn.fetchall())


@app.route('/task/', methods=['GET', 'POST'])
def task():
    if request.method == 'POST':
        return str(request.form['mindate'])

    d = sql.zz(sql.dep)
    return render_template('task.html', title='task', items=d.fetchall())


if __name__ == '__main__':
    app.run(debug=True)
