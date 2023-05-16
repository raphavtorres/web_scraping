import connect as con
import unidecode


def db_commit(sql, table=""):
    table = clean_input(table)
    try:
        for command in sql:
            con.cursor.execute(command)
    except Exception:
        sql = f"DROP TABLE {table}"
        con.cursor.execute(sql)
    con.db.commit()


def insert_db(table, title, price):
    table = clean_input(table)
    title = title.replace("Livro - ", "")
    price = price.replace("R$ ", "")

    sql = [
        f"INSERT INTO {table} (product_name, product_price) VALUES ('{title}', '{price}')"
    ]
    db_commit(sql)


def create_table(subject):
    subject = clean_input(subject)
    table = f"products{subject}"
    sql = [
        f"""
        CREATE TABLE {table} (
            id INT AUTO_INCREMENT,
            product_name VARCHAR(255) NOT NULL,
            product_price VARCHAR(255),
            PRIMARY KEY (id)
        );
        """
    ]
    db_commit(sql, table)


def select_products(subject):
    subject = clean_input(subject)
    table = f"products{subject}"
    sql = f"SELECT product_name, product_price FROM {table}"

    con.cursor.execute(sql)
    result = con.cursor.fetchall()
    return result


def clean_input(input):
    input = unidecode.unidecode(input)
    input = input.lower().replace("de-", "").replace("-", "_").replace(" ", "_")
    return input
