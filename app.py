from flask import Flask, render_template, redirect, url_for, request, flash
# from flask_login import login_user, login_required, logout_user
import sqlite3
from datetime import date

app = Flask(__name__)

global conn
global c

conn = sqlite3.connect('peo_form_answ.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS answ(
        a0 INTEGER,
        a1 TEXT,
        a2 INTEGER,
        a3 TEXT,
        a4 TEXT,
        a5 INTEGER,
        a6 INTEGER,
        a7 TEXT,
        a8 INTEGER,
        a9 INTEGER,
        a10 INTEGER,
        a11 INTEGER,
        a12 INTEGER,
        a13 INTEGER,
        a14 INTEGER,
        a15 INTEGER,
        a16 TEXT,
        a17 TEXT,
        a18 INTEGER,
        a19 TEXT,
        a20 INTEGER,
        a21 INTEGER,
        a22 TEXT,
        a23 TEXT,
        a24 INTEGER,
        a25 INTEGER,
        a26 INTEGER,
        a27 TEXT,
        a28 TEXT,
        a29 INTEGER,
        a30 TEXT,
        a31 TEXT,
        a32 TEXT,
        a33 TEXT,
        a34 INTEGER,
        a35 INTEGER,
        a36 INTEGER,
        a37 INTEGER,
        a38 TEXT
    )
""")
conn.commit()

l = {
    16: 6,
    22: 33,
    23: 29,
    30: 30,
    31: 13,
    32: 34,
    33: 7,
    38: 3,
}


@app.route("/ru", methods=['GET', 'POST'])
def login_page():

    data = []
    for i in range(0, 39):
        if i in l:
            data.append('')
            for j in range(0, l[i]):
                buf = request.form.get(str(i) + ' ' + str(j))
                if buf:
                    data[i] += str(buf) + ' '
        else:
            data.append(request.form.get(str(i)))

    print(data)
    if data:
        with sqlite3.connect("peo_form_answ.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO answ VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
            con.commit()
        message = "Спасибо за Ваши ответы!"
    else:
        message = "Заполните, пожайлуста, все поля"

    today = date.today()
    return render_template('form_ru.html', message=message, date=today.strftime("%Y-%m-%d"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
