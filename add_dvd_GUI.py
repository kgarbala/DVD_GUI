import MySQLdb, tkMessageBox
from Tkinter import *

def SQLAddDVD(Title, Star, Costar, Year, Genre):
    SQL = 'INSERT INTO dvd values("%s", "%s", "%s", "%s", "%s")' %\
    (Title, Star, Costar, Year, Genre)
    try: 
        db = MySQLdb.connect('localhost', 'root', 'niepowiem', 'dvdcollection')
        c = db.cursor()
        c.execute(SQL)
        db.commit()
        c.close()
        tkMessageBox.showinfo("Sukces", "Rekord zostal dopisany")
    except:
        tkMessageBox.showinfo("Blad", "Nie udalo sie dopisac rekordu")
   
def AddDVD():
    def getAll(event=None):
        Title = title.get()
        Star = star.get()
        Costar = costar.get()
        Year = year.get()
        Genre = genre.get()
        SQLAddDVD(Title, Star, Costar, Year, Genre)
          
    addFrame = Toplevel() 
    title = Entry(addFrame, bd=5)
    #title.focus_set()
    star = Entry(addFrame, bd=5)
    costar = Entry(addFrame, bd=5) 
    year = Entry(addFrame, bd=5) 
    genre = Entry(addFrame, bd=5) 
    OK = Button(addFrame, text='OK',width=15, command=getAll)  
    Cancel = Button(addFrame, text='Cancel',width=15, command=addFrame.destroy)
    genre.bind('<Return>', getAll)

    L0 = Label(addFrame, text="Tytul:")
    L1 = Label(addFrame, text="Star:")
    L2 = Label(addFrame, text="Costar:")
    L3 = Label(addFrame, text="Year:")
    L4 = Label(addFrame, text="Genre:")
    
    L0.grid(row=0, column=0)  
    L1.grid(row=1, column=0)     
    L2.grid(row=2, column=0)   
    L3.grid(row=3, column=0) 
    L4.grid(row=4, column=0) 
    
    title.grid(row=0,column=1)
    star.grid(row=1, column=1)
    costar.grid(row=2, column=1)
    year.grid(row=3, column=1)
    genre.grid(row=4, column=1)

    OK.grid(row=5, column=0)
    Cancel.grid(row=5, column=1)
