import sqlite3

with sqlite3.connect("test_database.db") as conn:
    cursor = conn.cursor()
    query = "SELECT * FROM People;"
    results = cursor.execute(query)
    print(results.fetchone())

