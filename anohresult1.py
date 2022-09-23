import xlsxwriter
from anoh import array

def writer(parametr):
    book = xlsxwriter.Workbook(r"C:\Users\organizer\pyproj\my_env\anoh.xlsx")
    page = book.add_worksheet("sheet")

    row = 0
    column = 0

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