import MySQLdb, csv, os

def writeCSV():
    SQL= "SELECT * FROM DVD"
    try:
        db = MySQLdb.connect("localhost", "root", "niepowiem", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL)
        output = c.fetchall()
        c.close()
        db.close()
    except:
        input("blad [Enter..]")
        return
    try:
        os.system('cls')
        print("Eksport")
        filename = raw_input("podaj nazwe pliku, bez csv:\n")
        filename += ".csv"
        writer = csv.writer(open(filename, "wb"))
        writer.writerow(("TITLE", "STAR", "COSTAR", "YEAR", "GENRE"))
        writer.writerows(output)
        print(filename, "zapis prawidlowy")
        raw_input("nacisnij [Enter..]")
        return
    except:
        print("Blad zapisu do pliku csv")
        raw_input("nacisnij [Enter..]")
        return
        
#writeCSV()
