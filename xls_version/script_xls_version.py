import os
import xlsxwriter
import math

myList = []
i=0
text= ''

#Filling your list, which will create your xls file.
#If you finish, just type stop 
#I do not know movie or distribution called "stop" :) 

def print_myList(mySequence):
    i=0
    for text in mySequence:
        i+=1

        if(i%2):
            print(text,  end = '')
        else:
            print("   ", text)


while text != 'stop':
    i+=1

    if(i%2):
        print_myList(myList)
        print()
        print("Nr", math.ceil(i/2), " title:")
        text = input("Give me Movie_Year text: ")    
    else:
        text = input("Give me Distrbution text: ")
        #for windows
        os.system("cls")
    if(text !='stop'):
        myList.append(text)


# Creating a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('bars.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

# Expanding the first columns to make the names visible
worksheet.set_column('A:B', 30)

# Writting the column headers.
worksheet.write('A1', 'Movie_Year', bold)
worksheet.write('B1', 'Distribution', bold)

# Start from first row after headers.
row = 1 
j=0

#writting data to specific cells
for text in myList:
    j+= 1
    if(j%2):
        worksheet.write(row, 0, text )
    else:
        worksheet.write(row, 1,text)
        row+= 1

workbook.close()


