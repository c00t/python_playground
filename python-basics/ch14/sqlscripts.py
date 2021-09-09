import sqlite3

sqlscripts = """
DROP TABLE IF EXISTS People;
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
);
INSERT INTO People VALUES (
    'Rex',
    'Temple',
    21
);
"""

with sqlite3.connect("test_database.db") as conn:
    cursor = conn.cursor()
    cursor.executescript(sqlscripts)
