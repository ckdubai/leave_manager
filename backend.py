import sqlite3

def create_offdays():
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS offdays (id INTEGER PRIMARY KEY, holiday text, days INTEGER, staff text)")
    conn.commit()
    conn.close()

def create_offtaken():
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS offtaken (sid INTEGER PRIMARY KEY, staff text, off_date text)")
    conn.commit()
    conn.close()

def insert(holiday,days,staff):
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO offdays VALUES(NULL,?,?,?)",(holiday,days,staff))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM offdays")
    rows=cur.fetchall()
    conn.close()
    return rows

def update(id,holiday,days,staff):
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    cur.execute("UPDATE offdays SET holiday=?, days=?, staff=? WHERE id=?",(holiday,days,staff,id))
    conn.commit()
    conn.close()

def search(holiday="",days="",staff=""):
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM offdays WHERE holiday=? OR days=? OR staff=?",(holiday,days,staff))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM offdays WHERE id=?",(id,))
    conn.commit()
    conn.close()

def insert_offtaken(staff,date):
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO offtaken VALUES(NULL,?,?)",(staff,date))
    conn.commit()
    conn.close()

def view_offtaken():
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM offtaken")
    rows=cur.fetchall()
    conn.close()
    return rows

def viewby_staffname(staff):
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM offtaken WHERE staff=?",(staff,))
    rows=cur.fetchall()
    conn.close()
    return rows

def get_off_status(staff):
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    rows_count = cur.execute("SELECT SUM(days) FROM offdays WHERE staff=?",(staff,))
    if  rows_count:
        total_days=cur.fetchall()
        for row in total_days:
            sum1=row[0]
        cur.execute("SELECT COUNT(staff) FROM offtaken WHERE staff=?",(staff,))
        off_days=cur.fetchall()
        for row in off_days:
            sum2=row[0]
        conn.close()
        if sum1 is not None :
           return sum1-sum2
    else:
        return 0


def delete_offtaken(id):
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM offtaken WHERE sid=?",(id,))
    conn.commit()
    conn.close()

def update_offtaken(id,staff,date):
    conn=sqlite3.connect("pendingOFF.db")
    cur=conn.cursor()
    cur.execute("UPDATE offtaken SET staff=?, off_date=? WHERE sid=?",(staff,date,id))
    conn.commit()
    conn.close()
