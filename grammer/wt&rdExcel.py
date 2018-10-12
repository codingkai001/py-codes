import xlrd
import xlwt


def read_excel():
    address = r'C:\Users\Coding-Kai\Desktop\excel\软件四班清明节离校同学信息.xls'
    workbook = xlrd.open_workbook(address)  # 打开指定的表格
    sheet1 = workbook.sheet_by_name('Sheet1')  # 根据sheet索引(by_index)或者名称获取sheet内容
    '''
    print(workbook.sheet_names())   # 获取所有sheet,返回一个列表
    
    print(sheet1.name)  # 获取名称
    print(sheet1.nrows)     # 获取行数
    print(sheet1.ncols)     # 获取列数
    '''
    for i in range(0, sheet1.nrows):
        if sheet1.row(i)[2].value != '':
            for j in range(0, sheet1.ncols):
                print(str(sheet1.row(i)[j].value).ljust(30), end='')
            print()


def write_excle():
    workbook = xlwt.Workbook()


if __name__ == '__main__':
    read_excel()
