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
    cur.execute("SELECT staff FROM offdays")
    rows=cur.fetchall()
    conn.close()
    # using list comprehension
    out = [item for row in rows for item in row]
    print(out)
    return out
