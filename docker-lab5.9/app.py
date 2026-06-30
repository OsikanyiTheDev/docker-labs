from flask import Flask, render_template, request, redirect
import mysql.connector
import time

app = Flask(__name__)

# Wait for MySQL to be ready (Docker-safe)
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

# ---------------------------
# SEED DEMO DATA (ONLY ONCE)
# ---------------------------
cursor.execute("SELECT COUNT(*) FROM students")
count = cursor.fetchone()[0]

if count == 0:
    demo_students = ["Osikanyi", "Ama", "Kofi", "Akosua", "Yaw"]

    cursor.executemany(
        "INSERT INTO students (name) VALUES (%s)",
        [(name,) for name in demo_students]
    )
    db.commit()
    print("Demo students inserted!")

# ---------------------------
# HOME + SEARCH (READ)
# ---------------------------
@app.route('/')
def home():
    search = request.args.get('search')

    if search:
        cursor.execute(
            "SELECT * FROM students WHERE name LIKE %s",
            ('%' + search + '%',)
        )
    else:
        cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()
    return render_template("index.html", students=students, search=search)

# ---------------------------
# CREATE
# ---------------------------
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    cursor.execute("INSERT INTO students (name) VALUES (%s)", (name,))
    db.commit()
    return redirect('/')

# ---------------------------
# DELETE
# ---------------------------
@app.route('/delete/<int:id>')
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

# ---------------------------
# EDIT PAGE
# ---------------------------
@app.route('/edit/<int:id>')
def edit_student(id):
    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()
    return render_template("edit.html", student=student)

# ---------------------------
# UPDATE
# ---------------------------
@app.route('/update/<int:id>', methods=['POST'])
def update_student(id):
    name = request.form['name']
    cursor.execute("UPDATE students SET name=%s WHERE id=%s", (name, id))
    db.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)