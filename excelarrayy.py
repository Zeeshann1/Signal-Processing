import xlrd
workbook = xlrd.open_workbook('AverageRSSI.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
data = [[worksheet.cell_value(r, c) for c in range(worksheet.ncols)] for r in range(worksheet.nrows)]
print(data[0])

