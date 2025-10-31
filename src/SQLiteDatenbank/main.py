import sqlite3

from datetime import datetime
from pathlib import Path

if __name__ == '__main__':
    
    print("Dieses Programm zeigt die nächsten Abfahrten an einer bestimmten Haltestellen-ID.")

    # Datenbankverbindung herstellen und Query vorbereiten
    connection = sqlite3.connect('datenbank.db3')
    
    sql_path: Path = Path('departures.sql')
    sql_text: str = sql_path.read_text(encoding='utf-8')

    dayname: str = datetime.now().strftime('%A').lower()
    sql_text = sql_text.format(dayname=dayname)

    while True:

        # Haltestellen-ID vom User holen
        stop_id: str = input("Haltestellen-ID: ")

        # Parameter erzeugen und SQL-Abfrage durchführen
        params: dict = {
            'stop_id': f"{stop_id}:%",
            'departure_time': datetime.now().strftime('%H:%M:%S'),
            'current_date': datetime.now().strftime('%Y%m%d')
        }

        cursor = connection.cursor()
        cursor.execute(sql_text, params)

        rows: list = cursor.fetchall()

        # Ergebnisse anzeigen
        print("")
        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")

        print("")
        

        