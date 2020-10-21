from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
import sqlite3

app = Flask(__name__)

global conn
global c

conn = sqlite3.connect('peo_form_answ.db')
c = conn.cursor()

c.execute(f"""
    CREATE TABLE IF NOT EXISTS ru(
        name TEXT,
        car TEXT
    )
""")
conn.commit()


@app.route("/ru", methods=['GET', 'POST'])
def login_page():

    name = request.form.get('name')
    car = request.form.get('cars')

    print(name, car)

    if name and car:
        message = "Спасибо за Ваш ответ"
        c.execute(f"INSERT INTO ru VALUES ('{name}', '{car}')")
        conn.commit()
    else:
        message = "Заполните, пожайлуста, все поля"

    return render_template('form_ru.html', message=message)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
