'''def getValues(a, pi=3.42,  c=None):
    if c is not None:
        print(c)
        return a+pi+c
    return a+pi
'''
'''def getdifference(a,b):
    if isinstance(a,(int,float)):
        return a-b
    else:
        print("pass either int or float")
        '''
'''print("hi")
if __name__ == '__main__':
    a=4
  #  b=8.6
   # print(getdifference(a,b))
print(getValues(a,10,5))'''
    #method overloading

import  xlrd
loc=("sample.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
shhet.cell_value(0,0)

for i in  renge(sheet.nrows):
    print(sheet.cell_value(i,1))



