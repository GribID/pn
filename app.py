from flask import Flask
import pyodbc

app = Flask(__name__)

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.120.52.101;DATABASE=Patio;UID=it;PWD=it')
cursor = cnxn.cursor()

@app.route('/')
def hello_world():
    cursor.execute('SELECT * FROM LV_Depositor')
    row1 = cursor.fetchall()
    return str(row1)


if __name__ == '__main__':
    app.run(debug=True)
