import sqlite3

create_table = """
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INT
);
"""
insert_data = """
INSERT INTO Roster VALUES (?, ?, ?);
"""
data = (
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
)

with sqlite3.connect("test_database.db") as conn:
    cursor = conn.cursor()
    # cursor.execute(create_table)
    cursor.executemany(insert_data, data)
    cursor.execute("UPDATE Roster SET Name='Ezri Dax' WHERE Name='Jadzia Dax';")
    cursor.execute("SELECT Name,Age From Roster WHERE Species='Bajoran' OR Species='Trill';")
    for row in cursor.fetchall():
        print(row)