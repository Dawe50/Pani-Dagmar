def zapsat(mail):
    import sqlite3
    conn = sqlite3.connect('otroci.db')
    c = conn.cursor()
    c.execute("SELECT email FROM users")
    rows=c.fetchall()
    jiz_zapsany=False
    for row in rows:
        akt_mail=str(row)
        if mail == akt_mail[2:-3]:
            jiz_zapsany=True
    if jiz_zapsany != True:
            conn = sqlite3.connect('otroci.db')
            c = conn.cursor()
            c.execute("SELECT MAX(id) FROM users")
            row=c.fetchone()
            cislo=row[0]+1
            c.execute("INSERT INTO users VALUES (?,?, 'n')", (cislo,mail))
            conn.commit()
            conn.close()
