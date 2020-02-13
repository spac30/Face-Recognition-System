import sqlite3

def Connect():
    conn = sqlite3.connect("./project1.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS project1(id INTEGER PRIMARY KEY, name TEXT, dob DATE, email TEXT, phone TEXT)")
    conn.commit()
    conn.close()
    
def Insert(name, dob, email, phone):
    conn = sqlite3.connect("./project1.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO project1 VALUES (NULL,?,?,?,?)",(name, dob, email, phone))
    conn.commit()
    conn.close()

def View():
    conn = sqlite3.connect("./project1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM project1")
    rows = cur.fetchall()
    conn.close()
    return rows

def Search(id):
    conn = sqlite3.connect("./project1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM project1 WHERE id = ?",(id,))
    rows = cur.fetchall()
    conn.close()
    return rows

def Last_Record():
    conn = sqlite3.connect("./project1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM project1 ORDER BY ID DESC LIMIT 1")
    rows = cur.fetchall()
    conn.close()
    return rows

def Delete(id):
    conn = sqlite3.connect("./project1.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM project1 WHERE id=?",(id,))
    conn.commit()
    conn.close()

def Update(id,name, dob, email, phone):
    conn = sqlite3.connect("./project1.db")
    cur = conn.cursor()
    cur.execute("UPDATE project1 SET name = ?, dob = ?, email = ?, phone = ? WHERE id = ?",(name, dob, email, phone, id))
    conn.commit()
    conn.close()    
    
    
# =============================================================================
# def search(name="", dob="", email="", phone="", gender=""):
#     conn = sqlite3.connect("project.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM project WHERE name = ?, dob = ?, email = ?, phone = ?, gender = ?",(name, dob, email, phone, gender))
#     rows = cur.fetchall()
#     conn.close()
#     return rows
# 
#print(search(name="yash"))
# =============================================================================
# =============================================================================
# connect()
# insert("yash","03-10-1996","yash@gmail.com",7490945663)
# view()   
# =============================================================================
#print(search("3"))