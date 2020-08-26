import os
import csv
import math
import tkinter 
from tkinter import font as tkFont
import time

def checkFS(text):
    if(text == 'f'or text =='s' ):
        return True
    else:
        return False

def print_myList(Movie, Dist):
    
    print("Your current saved data: ")

    if(len(Movie)==0):
        print("None")

    for i in range(0, len(Movie)):
        print(Movie[i],  end = '')
        print("   ", Dist[i])
    
    print()
    print("For example:")
    print("Movie_Year text - Kosmiczna jazda. Hau! Hau! Mamy problem! (2013)")
    print("Distribution text - Mówi Serwis")
    print()
    print("If you want copy last distribution name - type c")
    print("It is allowed only during distribution phase since saving Nr 1 bar")
    print()
    print("If you want delete last inserted title - type d")
    print()
    print("If you want finish - type s")

def clear_screen():
    #for windows
    os.system("cls")
    #for MAC, Linux
    #os.system("clear")

def check_SD(text):
    if(text !='s' and text !='d'):
        return True
    else:
        return False

def main():

    #list of movie_year elements
    myMovie = []
    #list of distribution elements
    myDist = []
    #the biggest list - visibility of diffferent bars with specific length 
    vl=[]

    i=0
    text = ''
    mode = ''

    print("Hello, PNK Bars Creator!")
    #setting film or serial mode
    while True:
        mode = input("Type f to create film bars, type s to create serial bars: ")
        print()

        if(checkFS(mode)):
            break
        else:
            print("Wrong mode. Try again.")

    #changing mode's type and value to help with indexing vl list
    if(mode=='f'):
        mode=5
    elif(mode=='s'):
        mode=0
    else:
        raise Exception ('Wrong mode.')

    #filling lists with Movie titles, years of production and distributions
    while text != 's':
        i+=1
        index = math.ceil(i/2)

        if(i%2):
            print_myList(myMovie, myDist)
            print()
            print("Nr", index , " title:")
            text = input("Give me Movie_Year text: ") 

            #deleting last list
            if(text=='d'):
                del myMovie[-1]
                del myDist [-1]
                i-=3
                clear_screen()

            if(check_SD(text)):
                myMovie.append(text)   
        else:
            text = input("Give me Distrbution text: ")
            #stop or delete statement
            if(text=='s'or text=='d'):
                del myMovie[-1]
                i-=2
            #copy statement
            if(text=='c' and index>1):
                myDist.append(myDist[-1])

            if(check_SD(text) and text !='c'):
                myDist.append(text) 
            clear_screen()

    #checking if length of myMovie is equal to myDist. It is necessary 
    if(len(myMovie)!=len(myDist)):
        print("myMovie: ", len(myMovie))
        print("myDist: ", len(myDist))
        raise Exception ('Length of Movie_Year list is not equal to Distribution list.')
        
    #setting of font
    tkinter.Frame().destroy()  
    arial7b = tkFont.Font(family='Arial', size=7, weight='bold')

    #calculating of the longest name of movie
    max=0
    for text in myMovie:
        width = arial7b.measure(text)
        if(width>max):
            max=width

    #dependency factor between value from script and Photoshop inch scale
    max*=11
    markLength=100

    #setting of bar length flag
    if(max<1300):
        markLength=4
    elif(max<1700):
        markLength=3
    elif(max<2100):
        markLength=2
    elif(max<2500):
        markLength=1
    elif(max<5700):
        markLength=0
    else:
        #name of Movie is too long
        raise Exception ('One of your Movie_Year text is too long for bar for 1920x1080 scene.')

    suppVar = 2*(mode+markLength)

    #print("myDist: ", len(myDist))
    #print("myMovie: ", len(myMovie))

    #creating vl list
    for i in range(0, 20):
        if(i==suppVar or i==(suppVar+1)):
            vl.append("true")
        else:
            vl.append("false")

    #creating csv file
    with open("output.csv",'w',newline='') as file_writer:

        fieldnames=['Movie_Year','Distribution', 'Sfull', 'SLfull', 'Shalf', 'SLhalf', 'S2_4', 'SL2_4', 'S2', 'SL2', 'S1_6', 'SL1_6', 'Ffull', 'FLfull', 'Fhalf', 'FLhalf', 'F2_4', 'FL2_4', 'F2', 'FL2', 'F1_6', 'FL1_6']

        writer=csv.DictWriter(file_writer,fieldnames=fieldnames)

        writer.writeheader()

        for i in range(0, len(myMovie)):
            writer.writerow({'Movie_Year': myMovie[i], "Distribution": myDist[i], 'Sfull': vl[0], 'SLfull': vl[1], 'Shalf': vl[2 ], 'SLhalf': vl[3 ], 'S2_4': vl[4 ], 'SL2_4': vl[5 ], 'S2': vl[6 ], 'SL2': vl[7 ], 'S1_6': vl[8 ], 'SL1_6': vl[9 ], 'Ffull': vl[10 ], 'FLfull': vl[11 ], 'Fhalf': vl[12 ], 'FLhalf': vl[13 ], 'F2_4': vl[14 ], 'FL2_4': vl[15 ], 'F2': vl[16 ], 'FL2': vl[17 ], 'F1_6': vl[18 ], 'FL1_6': vl[19 ]  })

    print("Csv file is successfully created.")
    time.sleep(2)

if __name__ == '__main__':
    main()

   