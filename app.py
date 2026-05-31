from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    conn = mysql.connector.connect(host="mysql",user="appuser",password='password123',database="employee_db")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    html = "<h1>Employee List</h1>"
    html += "<ul>"

    for emp in employees:
        html += f"<li>{emp[0]} - {emp[1]}</li>"

    html +="<ul>"

    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

