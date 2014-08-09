import MySQLdb

def ModifyDVD():
    try:
        dvdTitle = raw_input("Wproawdz tytul filmu do modyfikacji: ")
        SQL_LOOKUP = "SELECT * FROM DVD WHERE DVD_TITLE=\"%s\"" % dvdTitle
        db = MySQLdb.connect("localhost", "root", "niepowiem", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL_LOOKUP)
        searchResult = c.fetchall()
        if searchResult[0]==():
            raise 
    except:        
        print("Wystapil problem z dostepem do bazy danych")
        raw_input("Nacinij [Enter..]")
        return
    try:
        print ("1: Tytul\t", searchResult[0][0])
        print ("2: Star\t", searchResult[0][1])
        print ("3: Costar\t", searchResult[0][2])
        print ("4: Rok\t", searchResult[0][3])
        print ("5: Gatunek\t", searchResult[0][4])
        choice = raw_input("Wproadz liczbe[1:5]")
        titleChanged = False
        modify = ''
        newvalue = ''
        if choice=='1':
           modify = "DVD_TITLE"
           newvalueTitle = raw_input("Wprwadz tytul")
           newvalue = "\"%s\""% newvalueTitle
           titleChanged = True
        elif choice=='2':
		    modify = "DVD_STAR_NAME"
		    newvalue = raw_input("Wprwadz nazwisko osoby odtwarzajacej role pierwszoplanowa: ")
		    newvalue = "\"%s\""% newvalue
        elif choice=='3':
		    modify = "DVD_COSTAR_NAME"
		    newvalue = raw_input("Wprwadz nazwisko osoby odtwarzajacej role drugoplanowa: ")
		    newvalue = "\"%s\""% newvalue
        elif choice=='4':
		    modify = "DVD_YEAR"
		    newvalue = raw_input("Wprwadz rok produkcji")
		    newvalue = "\"%s\""% newvalue
        elif choice=='5':
            modify = "DVD_GENRE"
            newvalue = raw_input("Wprwadz gatunek")
            newvalue = "\"%s\""% newvalue
        else:
            print("Nic nie zmieniono")
            raw_input("Nacisnij [Enter..]")
            return
        SQL_UPDATE = "UPDATE DVD SET %s = %s WHERE DVD_TITLE = \"%s\""  \
		% (modify, newvalue, dvdTitle)
  	
        db = MySQLdb.connect("localhost", "root", "niepowiem", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL_UPDATE)
        db.commit()

        if titleChanged:
            SQL_LOOKUP = "SELECT * FROM DVD WHERE DVD_TITLE = \"%s\"" %newvalueTitle		
        c = db.cursor()
        c.execute(SQL_LOOKUP)
        modifyResult = c.fetchall()
        c.close()
        db.close()

    except:
        print ("Wyspatpil problem z dostepem do rekordu w bazie danych")
        raw_input("nacinij [Enter..]")
        return
   
    print ("Nowa zawartosc rekordu:")
    print ("1: Tytul\t", modifyResult[0][0])
    print ("2: Star\t", modifyResult[0][1])
    print ("3: Costar\t", modifyResult[0][2])
    print ("4: Rok\t", modifyResult[0][3])
    print ("5: Gatunek\t", modifyResult[0][4])
    raw_input("Nacinij [Enter..]")
