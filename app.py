from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# connect to SQLite (just a file, no server needed)
db = sqlite3.connect("students.db", check_same_thread=False)
cursor = db.cursor()

# create the table if it doesn't exist yet
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        program TEXT,
        start_date TEXT,
        end_date TEXT
    )
""")
db.commit()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        age = request.form["age"]
        program = request.form["program"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

        cursor.execute("""
            INSERT INTO students (first_name, last_name, age, program, start_date, end_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, age, program, start_date, end_date))
        db.commit()
        return redirect("/view")
    return render_template("add.html")


@app.route("/remove", methods=["GET", "POST"])
def remove():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        cursor.execute("DELETE FROM students WHERE first_name = ? AND last_name = ?", (first_name, last_name))
        db.commit()
        return redirect("/view")
    return render_template("remove.html")


@app.route("/view")
def view():
    return render_template("view.html")


@app.route("/get_students")
def get_students():
    cursor.execute("SELECT id, first_name, last_name, age, program, start_date, end_date FROM students")
    students = cursor.fetchall()
    return {"students": students}


if __name__ == "__main__":
    app.run(debug=True)