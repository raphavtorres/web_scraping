import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='fastshop_scraper'
)

cursor = db.cursor()
