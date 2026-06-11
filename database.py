import sqlite3

# Connect to database (creates database if not exists)
conn = sqlite3.connect("registration.db")

# Create cursor object
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS registration (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    course TEXT NOT NULL
)
""")

print("Table created successfully!")

# ---------------- CREATE ----------------
cursor.execute("""
INSERT INTO registration (name, email, course)
VALUES (?, ?, ?)
""", ("Susmitha", "susmitha@gmail.com", "Python"))

conn.commit()
print("Record inserted successfully!")

# ---------------- READ ----------------
print("\nAll Records:")
cursor.execute("SELECT * FROM registration")
records = cursor.fetchall()

for row in records:
    print(row)

# ---------------- UPDATE ----------------
cursor.execute("""
UPDATE registration
SET course = ?
WHERE id = ?
""", ("Python Development", 1))

conn.commit()
print("\nRecord updated successfully!")

# Display updated records
cursor.execute("SELECT * FROM registration")
print("\nAfter Update:")
for row in cursor.fetchall():
    print(row)

# ---------------- DELETE ----------------
cursor.execute("""
DELETE FROM registration
WHERE id = ?
""", (1,))

conn.commit()
print("\nRecord deleted successfully!")

# Display remaining records
cursor.execute("SELECT * FROM registration")
print("\nAfter Delete:")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()

print("\nDatabase connection closed.")
