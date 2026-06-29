from flask import Flask, render_template
import mysql.connector
import time

app = Flask(__name__)

# Wait for DB
while True:
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="rootpass",
            database="labdb"
        )
        cursor = db.cursor()
        print("Connected to MySQL!")
        break
    except:
        print("Waiting for MySQL...")
        time.sleep(2)


# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
)
""")

db.commit()

# Insert sample data (avoid duplicates later if you want improvement)
cursor.execute("INSERT INTO students (name) VALUES ('Osikanyi')")
db.commit()


@app.route('/')
def home():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)