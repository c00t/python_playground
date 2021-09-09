import sqlite3

with sqlite3.connect("test_database.db") as conn:
    cursor = conn.cursor()
    query = "SELECT * FROM People;"
    results = cursor.execute(query)
    print(results.fetchone())
    edit_query = "UPDATE People SET Age=? WHERE FirstName=? AND LastName=?;"
    cursor.execute(edit_query, (42, 'Rex', 'Temple'))

