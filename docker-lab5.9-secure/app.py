from flask import Flask, render_template, request, redirect
import mysql.connector
import os
import time

app = Flask(__name__)

# Wait for DB
while True:
    try:
        db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = db.cursor()
        print("Connected to MySQL!")
        break
    except:
        print("Waiting for MySQL...")
        time.sleep(2)

@app.route('/')
def home():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template("index.html", students=students)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    cursor.execute("INSERT INTO students (name) VALUES (%s)", (name,))
    db.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()
    return render_template("edit.html", student=student)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    cursor.execute("UPDATE students SET name=%s WHERE id=%s", (name, id))
    db.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)