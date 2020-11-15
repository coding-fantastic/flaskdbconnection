import  MySQLdb

def connection():
    conn = MySQLdb.connect (host="localhost",
                                user = "root",
                                passwd = "",
                                db = "fla_mysql")
    c = conn.cursor()

    return c, conn