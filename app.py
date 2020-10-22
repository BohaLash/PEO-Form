from flask import Flask, render_template, redirect, url_for, request, flash
# from flask_login import login_user, login_required, logout_user
from flask import send_file
import sqlite3
import csv
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
        a38 INTEGER,
        a39 TEXT
    )
""")
conn.commit()

l = {
    16: 6,
    22: 33,
    23: 29,
    30: 31,
    31: 13,
    32: 34,
    33: 7,
    35: 6,
    39: 3,
}

answs = [
    ['Ukraine',
     'Weißrussland',
     'Russland',
     'Moldau',
     'Polen',
     'Litauen',
     'Lettland',
     'Estland',
     'Georgien',
     'Armänien'],  # 0
    [],  # 1
    ['Herr',
     'Frau'],  # 2
    [],  # 3
    [],  # 4
    ['nein',
     'ja'],  # 5
    ['nein',
     'ja'],  # 6
    [],  # 7
    [],  # 8
    [],  # 9
    ['Ukraine',
     'Weißrussland',
     'Russland',
     'Moldau',
     'Georgien',
     'Armänien',
     'EU'],  # 10
    ['nein',
     'ja'],  # 11
    ['nein',
     'ja'],  # 12
    ['nein',
     'ja'],  # 13
    [],  # 14
    [],  # 15
    ['keine',
     'Katzen',
     'Hunde',
     'Latex',
     'Chemiekalien'],  # 16
    [],  # 17
    ['nein',
     'ja'],  # 18
    [],  # 19
    ['nein',
     'ja'],  # 20
    ['nein',
     'ja'],  # 21
    ['zuverlässig',
     'geduldig',
     'kommunikationsfreudig',
     'motiviert',
     'ausgegliechen',
     'energisch',
     'erfahren',
     'ruhig',
     'organisiert',
     'aufrichtig',
     'ehrgeizig',
     'selbstdiszipliniert',
     'stressresistent',
     'aufmerksam',
     'ordentlich',
     'fleißig',
     'gutherzig',
     'ich lerne schnell neue Sachen',
     'Ich habe keine schlechten Gewohnheiten',
     'freundlich',
     'gewissenhaft',
     'immer optimistisch',
     'empathisch',
     'ich versuche zu jedem Menschen einen Draht zu finden',
     'manchmal nachdrücklich',
     'kreativ',
     'vielseitig',
     'ausgegliechen',
     'homorvoll',
     'gewissenhaft',
     'selbstdiszipliniert',
     'aufgeschlossen',
     'ordentlich, Sauberkeit'],  # 22
    ['Sport machen',
     'Bücher und Journals lesen',
     'Zeitung lesen',
     'Brettspiele spielen',
     '"Mensch ärger dich nicht" spielen',
     'Schach',
     'Damen',
     'Karten',
     'Fernsehen',
     'spazierengehen in der Natur',
     'mit meinem Hund spazieren gehen',
     'Kreuzworträtzel lösen',
     'stricken',
     'deutsch lernen',
     'in Chor singen',
     'Karaoke singen',
     'malen',
     'holzschnitzen',
     'handwerken zu Hause',
     'ich gehen regelmäßig',
     'kochen',
     'backen',
     'Gedichte dichten und Poesie',
     'Faltendes Origami-Papier',
     'ich arbeite gern in meinem Garten',
     'mit meinen Haustieren spielen',
     'mit meiner Familie Zeit verbringen',
     'reisen',
     'fotografieren und Fotos bearbeiten'],  # 23
    [],  # 24
    ['leider kann ich nicht so gut kochen',
     'als Hausfrau koche zu Hause für mich und für meine Familie.',
     'ich koche sehr gerne und probiere oft neuen Rezepte aus.',
     'kochen und acken ist mein großes Hobby!'],  # 25
    [],  # 26
    [],  # 27
    [],  # 28
    ['Herr',
     'Frau',
     'Ehepaar'],  # 29
    ['die Person im Bett drehen',
     'transfer der von Rollstuhl ins Bett',
     'hilfestellung bei Treppensteigung',
     'hilfe bei An- und Auskleiden',
     'die Person im Bett waschen',
     'den Oberkörper waschen',
     'Beine und Intimbereich waschen',
     'Mundpflege',
     'Fusspflege',
     'Haarpflege',
     'Hilfestellung beim Toilettengang geben',
     'Windeln wechseln',
     'leeren des Harnbeutels',
     'leeren des Stomabeutels',
     'helfen, Konjunktivfähigkeiten zu reaktivieren',
     'Essenreichen',
     '?',
     'Flüssigkeitsaufnahme kontrollieren',
     'kochen und das Diät der Person berücksichtigen',
     'das Haushalt machen',
     'Einkaufen von Lebensmitteln',
     'kochen',
     'Pflege von Pflanzen',
     'Gartenpflege',
     'Pflege von Haustieren',
     'gemeinsame Spaziergänge machen',
     '?',
     'Begleitung zu Arztterminen',
     'Kontrolle der Medikamenteneinnahme',
     'sporadische nächtliche Einsätze',
     'reguläre nächtlihe Einsätze'],  # 30
    ['keine',
     'Rollator',
     'Rollstuhl',
     'elektricher Rollstuhl',
     'Pflegebett',
     'Patientenlifter',
     'Dekubitus Matratze',
     'Treppenlift',
     'Duschstuhl',
     'Urinflache',
     'Windeln',
     'Bettvorlagen',
     'Toilettenstuhl'],  # 31
    ['zwei Patienten im Haushalt',
     'Allergien',
     'Alzheimer',
     'Asthma',
     'Hypertonie',
     'Depression',
     'Diabetes',
     'Diabetes (Insulitspritzen nötig)',
     'Schlaganfall',
     'Atemhilfe und Sauerstoffmaske',
     'Essen Einnahme üner PEG Sonde',
     'Katheter',
     'Stoma',
     'Unterstützung bei der Mobilität',
     'Transfer von Rollstuhl ins Bett',
     'bettlägerige Patienten',
     'gestörtes Schlaf- Wachrytmus',
     'Allergien',
     'StuhlInkontinenz',
     'Harninkontindnz',
     'Krebs',
     'Osteoporose',
     'Parkinson',
     'Herzinfarkt',
     'Schlaganfall',
     'Multiple Sklerose',
     'Rheumatismus',
     'Herzrhythmusstörung',
     'Herzinsuffizienz',
     'Leichte Demenz',
     'Mittelschwere Demenz',
     'Schwere Demenz',
     'altersbedingte Gehschwäche',
     'keine Erfahrung'],  # 32
    ['Erste Hilfe Kurs',
     'Massagekurs',
     'Kochkurs',
     'Diätologiekurs',
     'Betreuer Kurs',
     'Andere',
     'keine'],  # 33
    ['nein',
     'ja'],  # 34
    ['noch in der Schule',
     'Sprachhkurse',
     'auf angebotenen Sprachkursen von Medius Work',
     'bei der Arbeit',
     'Eigenständig',
     'nicht gelernt'],  # 35
    ['weniger als 3 Monate',
     'über 3 Monate',
     'über 6 Monaten',
     'über 1 Jahr'],  # 36
    ['fließend deutsch',
     'fortgeschrittes Sprachniveau',
     'kommunikatives Sprachniveau',
     'kaum deutsch'],  # 37
    ['Göthe C1',
     'Göthe B2',
     'Göthe B1',
     'Göthe A2',
     'Göthe A1'],  # 38
    ['polnisch',
     'englisch',
     'italienisch']  # 39
]

path = {
    'ru': 'form_ru.html',
    'ua': 'form_ua.html',
    'pl': 'form_pl.html',
}


def parse_to_cvs(path):
    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        with sqlite3.connect("peo_form_answ.db") as con:
            cur = con.cursor()
            # for each row in db fetch data to the output list
            for row in cur.execute("SELECT * FROM answ"):
                output = []
                for i in range(0, 40):
                    # if question has options
                    if answs[i]:
                        # if question has checkboxes
                        if i in l:
                            output.append('')
                            if row[i]:
                                for j in row[i][0:-1].split(' '):
                                    output[i] += answs[i][int(j)] + ';    '
                        else:
                            output.append('')
                            output[i] = answs[i][int(row[i])]
                    else:
                        output.append(row[i])
                # put list of fetched data in csv table
                writer.writerow(output)


@ app.route("/<language>", methods=['GET', 'POST'])
def login_page(language):
    # get data from form
    data = []
    for i in range(0, 40):
        # if question has options
        if i in l:
            data.append('')
            for j in range(0, l[i]):
                buf = request.form.get(str(i) + ' ' + str(j))
                if buf:
                    data[i] += str(buf) + ' '
        else:
            data.append(request.form.get(str(i)))

    # put data to the db if avalible
    if data[1] != None and data[3] != None and data[4] != None:
        with sqlite3.connect("peo_form_answ.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO answ VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
            con.commit()
        message = "Спасибо за Ваши ответы!"
    else:
        message = "Заполните, пожайлуста, все поля"

    today = date.today()
    return render_template(path[language], message=message, date=today.strftime("%Y-%m-%d"))


@app.route('/download')
def downloadFile():
    path = "output.csv"
    parse_to_cvs(path)
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
