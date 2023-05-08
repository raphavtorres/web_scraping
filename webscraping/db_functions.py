import connect as con

def db_commit(sql, table=""):
    try:
        for command in sql:
            con.cursor.execute(command)
    except Exception:
        sql = f"DROP TABLE {table}"
        con.cursor.execute(sql)
    con.db.commit()


# Mudar info
def insert_db(table, year, contest, numbers, date="00/00/0000"):
    n1, n2, n3, n4, n5, n6 = numbers
    sql = [
        f"INSERT INTO {table} (megaYear, contest, n1, n2, n3, n4, n5, n6, dateMega) VALUES ({year}, {contest}, {n1}, {n2}, {n3}, {n4}, {n5}, {n6}, '{date}')"
    ]
    db_commit(sql)