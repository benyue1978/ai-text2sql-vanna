import sqlite3

conn = sqlite3.connect("mydb.sqlite")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25), ('Charlie', 35)")
conn.commit()
conn.close()
print('数据库初始化完成') 