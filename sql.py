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
