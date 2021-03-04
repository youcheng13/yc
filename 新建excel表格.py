import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
cell =sheet['A1']
cell.value = '你好中国'
wb.save('表格测试excel.xlsx')
