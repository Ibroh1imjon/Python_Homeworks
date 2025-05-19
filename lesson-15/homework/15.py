import sqlite3

# ------- 1 -------
with sqlite3.connect("my_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
    """)
    print("Database and table created successfully.")


# ------- 2 -------
roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

with sqlite3.connect("my_database.db") as conn:
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
    """)

    cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", roster_data)

    print("Data inserted successfully.")



# ------- 3 -------
with sqlite3.connect("my_database.db") as conn:
    cursor = conn.cursor()
    
    cursor.execute("""
    UPDATE Roster
    SET Name = ?
    WHERE Name = ?
    """, ("Ezri Dax", "Jadzia Dax"))

    print("Name updated successfully.")


# ------- 4 -------
with sqlite3.connect("my_database.db") as conn:
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
    """)
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
