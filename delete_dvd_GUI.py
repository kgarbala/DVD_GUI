import MySQLdb
from Tkinter import *
import tkMessageBox

def SQLDeleteDVD(dvdToDelete):
    try:
        SQL_DELETE = "DELETE DVD FROM DVD WHERE DVD_TITLE = \
        \"%s\"" % dvdToDelete
        db = MySQLdb.connect("localhost", "root", "niepowiem", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL_DELETE)
        db.commit()
        c.close()
        db.close()
        raw_input("Rekord zostal usuniety")         
    except:
        print("wystapil problem z usunieciem rekordu z bazy")
        raw_input("Nacisnij [Enter..]")
        return 
def DeleteDVD():
    '''
    dvdToDelete= raw_input("\nWprowadz tytul do usuniecia: ")
    SQL_LOOKUP = "SELECT * FROM DVD WHERE DVD_TITLE = \
    \"%s\"" % dvdToDelete
    try:
        db = MySQLdb.connect("localhost", "root", "niepowiem", "DVDCOLLECTION")
        c=db.cursor()
        c.execute(SQL_LOOKUP)
        searchResult= c.fetchall()
        if searchResult[0]==():
            raise
    except:
        print ("Wystapil problem z dostepem do rekordu w bazie")
        raw_input("Nacisnij [Enter..]")
        return
    print("Usuwany rekord:")
    print ("1: Tytul\t", searchResult[0][0])
    print ("2: Star\t", searchResult[0][1])
    print ("3: Costar\t", searchResult[0][2])
    print ("4: Rok\t", searchResult[0][3])
    print ("5: Gatunek\t", searchResult[0][4])
    print("czy na pewno chcesz usunac?\nT/t = tak, inny znak = nie")
    choice=raw_input("\t")
    if choice=="T" or choice=="t":
       SQLDeleteDVD(dvdToDelete)
    else:
        c.close()
        db.close()
        raw_input("Rekord nie zostal usuniety, nacisnij [Enter..]")
    '''  
    def delDVD(event=None): 
        pass
        
    def findDVD(event=None):
        dvdToDelete=E.get()
        SQL_LOOKUP = "SELECT * FROM DVD WHERE DVD_TITLE =\
             \"%s\"" % dvdToDelete
        print(SQL_LOOKUP)
        try:
            db = MySQLdb.connect("localhost", "root", "niepowiem", "DVDCOLLECTION")
            c = db.cursor()
            c.execute(SQL_LOOKUP)
            searchResult = c.fetchall()
        except:
            tkMessageBox.showinfo("Blad", "Nie udalo sie polaczyc z baza")
            return   
        s=['']*6            
        for entry in searchResult:
            s[0]= "==============="
            s[1]= "Tytul:                          = "+ entry[0]
            s[2]= "Rola glowna:             = "+ entry[1]
            s[3]= "Rola drugoplanowa:= "+ entry[2]
            s[4]= "Rok:                            = "+ entry[3]
            s[5]= "Gatunek:                    = "+ entry[4]       
            for k in range(len(s)):          
                Lbox.insert(END, s[k])
        
    delFrame = Tk()
    delFrame.minsize(100, 100), delFrame.title("Delete DVD")
    L=Label(delFrame, text="DVD to delete")
    E=Entry(delFrame); #E.bind('<Return>', delDVD)
    B0=Button(delFrame, text="DELETE", command=delDVD)
    B1=Button(delFrame, text="CANCEL", command=delFrame.destroy)
    B2=Button(delFrame, text="FIND", command=findDVD)
    Lbox=Listbox(delFrame)

    L.pack()
    E.pack()
    B0.pack()
    B1.pack()
    B2.pack()
    Lbox.pack()
 
    #L.gird(row=0, column=1)
    #E.grid(row=1, column=0)   
    #B.grid(row=2, column=0) 
    #Lbox.grid(row=0, column=1)        
    delFrame.mainloop() 
    
#DeleteDVD()
