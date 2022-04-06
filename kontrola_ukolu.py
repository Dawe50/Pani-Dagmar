def zkontrolovat():
    import sqlite3
    conn = sqlite3.connect('otroci.db')
    c = conn.cursor()
    c.execute("SELECT email FROM users WHERE splneno='y'")
    rows=c.fetchall()
    seznam_adres=""
    for row in rows:
        adresa=str(row)
        seznam_adres+=adresa[2:-3]
    conn.commit()
    conn.close()

zkontrolovat()
    

