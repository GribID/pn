import pyodbc


def zz(sqlreq):
#   cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.120.52.101;DATABASE=Patio;UID=it;PWD=it')
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.120.52.101;DATABASE=Patio;UID=it;PWD=it')
    cursor = cnxn.cursor()
    return cursor.execute(sqlreq)


dep = '''
SELECT * 
FROM LV_Depositor
'''

order = '''
SELECT * 
FROM LV_Order 
WHERE ord_InputDate > GETDATE()-1 
ORDER BY ord_InputDate DESC
'''

order_item = '''
SELECT * 
FROM LV_OrderItem INNER JOIN
LV_ProductLang ON LV_OrderItem.ori_ProductID = LV_ProductLang.prdl_ProductID 
  AND LV_ProductLang.prdl_LanguageID = 4 
WHERE ori_OrderID = 
'''
