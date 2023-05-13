import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='web_scraping'
)

cursor = db.cursor()
