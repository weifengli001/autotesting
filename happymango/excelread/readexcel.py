import xlrd

def read_excel(file_name, sheetindex, rowindex, colindex):
    file_location = file_name
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_index(sheetindex)
    #print sheet.cell(rowindex, colindex)
    return sheet.cell(rowindex, colindex).value

