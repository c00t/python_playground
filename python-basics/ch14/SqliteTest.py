import sqlite3

# test1
# connection = sqlite3.connect(":memory:")
# cursor = connection.cursor()
# query = "SELECT datetime('now', 'localtime');"
# results = cursor.execute(query)
# print(results)
# print(results.fetchone())
# connection.close()

create_table = """
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
);
"""

insert_data = """
INSERT INTO People VALUES (
    "Rex",
    "Temple",
    21
);
"""

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
# cursor.execute(create_table)
cursor.execute(insert_data)

connection.commit()
connection.close()