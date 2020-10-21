from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
import sqlite3
from datetime import date

app = Flask(__name__)

today = date.today()

global conn
global c

conn = sqlite3.connect('peo_form_answ.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS answ(
        sex BOOLEAN,
        car DECIMAL(1,0)
    )
""")
conn.commit()


@app.route("/ru", methods=['GET', 'POST'])
def login_page():

    name = request.form.get('name')
    car = request.form.get('cars')

    print(name, car)

    if name and car:

        with sqlite3.connect("peo_form_answ.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO answ VALUES (?, ?)", [name, car, ])
            con.commit()
            message = "Спасибо за Ваш ответ"
    else:
        message = "Заполните, пожайлуста, все поля"

    return render_template('form_ru.html', message=message, date=today.strftime("%Y-%m-%d"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
