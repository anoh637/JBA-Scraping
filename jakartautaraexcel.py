# 2. This is the excel output for jakartautara.py

# 2.1. Import the needed library
# Before importing the libraries; on your terminal environment, install the module: pip install xlsxwriter
import xlsxwriter # This is to convert the code to excel
from jakartautara import array # 'run' is the name of run.py file, 'array' is the final looping name we wanted to print

def writer(parametr):
    book = xlsxwriter.Workbook(r"C:\Users\organizer\pyproj\my_env\jakartautara.xlsx") # this is to create a new excel, choose the path you wanted to save the file
    page = book.add_worksheet("sheet") # this is to create a sheet in your excel, choose the name of your sheet

    # all row and column starts from 0
    row = 0
    column = 0

    # in the output, we have 11 items to be displayed, create column and rows 11 times
    page.set_column("A:A", 1)
    page.set_column("B:B", 1)
    page.set_column("C:C", 1)
    page.set_column("D:D", 1)
    page.set_column("E:E", 1)
    page.set_column("F:F", 1)  
    page.set_column("G:G", 1)
    page.set_column("H:H", 1)
    page.set_column("I:I", 1)
    page.set_column("J:J", 1)
    page.set_column("K:K", 1)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        page.write(row, column+5, item[5])
        page.write(row, column+6, item[6])
        page.write(row, column+7, item[7])
        page.write(row, column+8, item[8])
        page.write(row, column+9, item[9])
        page.write(row, column+10, item[10])
        row +=1
    book.close() 
writer(array)