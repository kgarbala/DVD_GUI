import MySQLdb
from Tkinter import *
import tkMessageBox

def SQLLookupDVD(searchby, searchtext):  
    SQL = "SELECT * FROM DVD WHERE %s=\"%s\"" % (searchby, searchtext)  
    try:
        db = MySQLdb.connect("localhost", "root", "niepowiem", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL)
        output = c.fetchall()
        c.close()
        db.close()       
    except:
        tkMessageBox.showinfo("Blad", "Nie udalo sie polaczyc z baza")
        return
        
    if not output:
        L3.config(text='Brak rekordow')
        return
    else: 
        L3.config(text='')
        
    SQLlookFrame = Toplevel(); SQLlookFrame.minsize(200, 300)
    SQLlookFrame.title("Wyniki wyszukiwania")
    S=Scrollbar(SQLlookFrame)
    S.pack( side = RIGHT, fill=Y )  
    L=Listbox(SQLlookFrame, yscrollcommand=S.set, width=60)
        
    s=['']*6  
    result='Wyniki wyszukiwania: \n'
    for entry in output:
        s[0]= "==============="
        s[1]= "Tytul:                          = "+ entry[0]
        s[2]= "Rola glowna:             = "+ entry[1]
        s[3]= "Rola drugoplanowa:= "+ entry[2]
        s[4]= "Rok:                            = "+ entry[3]
        s[5]= "Gatunek:                    = "+ entry[4]       
        for k in range(len(s)):          
            L.insert(END, s[k])
            
    L.pack( side = LEFT, fill = BOTH )
    S.config( command = L.yview )  
    return
    
def LookupDVD():
    global  L3
    dict={0: "DVD_TITLE", 1: "DVD_STAR_NAME", 2: "DVD_COSTAR_NAME", \
        3: "DVD_YEAR", 4: "DVD_GENRE"}
        
    def getQuery(event=None): 
        searchby = dict[var.get()]
        searchtext = E.get()               
        SQLLookupDVD(searchby, searchtext)
        
    lookFrame = Toplevel()
    lookFrame.minsize(100, 100), lookFrame.title("LookupDVD")
    var = IntVar()
    R1 = Radiobutton(lookFrame, text="Title ", variable=var, value=0)    
    R2 = Radiobutton(lookFrame, text="Star  ", variable=var, value=1)                 
    R3 = Radiobutton(lookFrame, text="Costar", variable=var, value=2)                    
    R4 = Radiobutton(lookFrame, text="Year  ", variable=var, value=3)                   
    R5 = Radiobutton(lookFrame, text="Genre ", variable=var, value=4)
    E=Entry(lookFrame)
    E.bind('<Return>', getQuery)
    B = Button(lookFrame, text="OK", command=getQuery)
    L = Label(lookFrame)
    R2.select()
    R1.grid(row=0, column=0)  
    R2.grid(row=1, column=0)     
    R3.grid(row=2, column=0)   
    R4.grid(row=3, column=0) 
    R5.grid(row=4, column=0)    
    
    E.grid(row=0, column=1)   
    B.grid(row=1, column=1) 
    L3 = Label(lookFrame)
    L3.grid(row=2, column=1)      
    lookFrame.mainloop()
#LookupDVD()