# DVD.PY
# PROGRAM DO ZARZADZANIA BAZA DANYCH KOLEKCJI FILMOW
# POWSTAL NA PODSTAWIE PROJEKTU JAMES'A O. KNOWLTON'A
# W KSIAZCE "PYTHON PROJEKTY DO WYKORZYSTANIA". 
# Python: 2.7
# MySQL 5.6.19 Community Server (GPL)
# Platoforma: Windows
# KRZYSZTOF GARBALA

from Tkinter import *
import os
import add_dvd_GUI, lookup_dvds_GUI, modify_dvd_GUI, delete_dvd_GUI, csvreport_dvd_GUI

def menu():
    global choice
    #os.system('cls')
    print(''' Baza Filmow:
    1. dodaj
    2. przeszukaj
    3. modyfikuj
    4. usun
    5. eksportuj csvreport_dvd
    6. Koniec
    ''')
    choice =input("Wybierz opcje:")
    return choice
choice=''
'''
while choice!=6:
    choice=menu()
    os.system('cls')
    if choice==1:         
        add_dvd_GUI.AddDVD()
        os.system('cls')
    elif choice==2:
        os.system('cls')
        lookup_dvds_GUI.LookupDVD()
    elif choice==3:
        os.system('cls')
        modify_dvd_GUI.ModifyDVD()
    elif choice==4:
        os.system('cls')
        delete_dvd_GUI.DeleteDVD()
    elif choice==5:
        os.system('cls')
        csvreport_dvd_GUI.writeCSV()        
    else:
        if choice !=6:
            os.system('cls')
'''

frame = Tk()
frame.minsize(300, 300), frame.title("DVD Collection")
addDVD = Button(frame, text= "Dodaj film", width=20, command=add_dvd_GUI.AddDVD).pack()
lookDVD = Button(frame, text= "Szukaj filmu", width=20, command=lookup_dvds_GUI.LookupDVD).pack()
moodDVD = Button(frame, text= "Modyfikuj film", width=20, command=modify_dvd_GUI.ModifyDVD).pack()
delDVD = Button(frame, text= "Usun film", width=20, command= delete_dvd_GUI.DeleteDVD).pack()
expDVD = Button(frame, text= "Elsportuj kolekcje", width=20, command=csvreport_dvd_GUI.writeCSV).pack()
quit = Button(frame, text= "Zakoncz", width=20, command=frame.destroy).pack()
frame.mainloop()