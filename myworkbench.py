import mysql.connector


def connectToDB(dbname,password):
    user='root'
    host='localhost'
    password=password
    database=dbname

    conn=mysql.connector.connect(user=user,host=host,password=password,database=database)
    return conn


def selectFromTable(tablename,conn,attribute):
    if len(attribute)==0:
        users="SELECT * FROM "+tablename
    else:
        users="SELECT "
        for i in range(len(attribute)):
            if(i<len(attribute)-1):
                users+=attribute[i]
                users+=','
            else:
                users+=attribute[i]
        users+=" FROM "+tablename

    cursor = conn.cursor()
    cursor.execute(users)
    print(users)
    result=cursor.fetchall()
    for i in result:
        print(i)

def showTables(conn):
    show="SHOW TABLES"
    cursor = conn.cursor()
    cursor.execute(show)
    result=cursor.fetchall()
    return result

def updateTable(attribute,tablename,where,key,conn):
    update="UPDATE "+tablename+" SET "
    if(len(attribute)>0):
        j=0
        for i in attribute:
            if(j<len(attribute)-1):
                update+=i
                update+=" = '"
                update+=attribute[i]
                update+="' , "
            else:
                update+=i
                update+=" = '"
                update+=attribute[i]
                update+="' "
            j+=1
    update+='WHERE '
    if(len(where)>0):
        j=0
        for i in where:
            if(j<len(where)-1):
                update+="`"+i+"`"
                update+=" = '"
                update+=where[i]
                update+="' "+key+" "
            else:
                update+="`"+i+"`"
                update+=" = '"
                update+=where[i]
                update+="' "
            j+=1
    print(update)
    cursor = conn.cursor()
    cursor.execute(update)
    conn.commit()

def deletefromtable(tablename,attribute,key):
    delete=' DELETE FROM '+tablename+' where '+attribute+'="'+key+'"'
    cursor = conn.cursor()
    cursor.execute(delete)
    conn.commit()

def search(tablename,attribute,key):
    search=' Select '+attribute+' from '+tablename+' where '+attribute+'="'+key+'"'
    cursor = conn.cursor()
    cursor.execute(search)
    print(search)

    while True:
        rows=cursor.fetchone()
        if rows==None:
            break
        print(rows)    
    





conn=connectToDB('airlineres','')
#Test cases
#search('passenger_profile','First_name',"Kaustubh")
#d={'First_name':'Mohit',
#'Last_name':'Khede'}
#w={'password':'rst'}
#updateTable(d,'passenger_profile',w,'and',conn)


#deletefromtable('passenger_profile','First_name',"Mohit")
#selectFromTable('passenger_profile',conn,[])
