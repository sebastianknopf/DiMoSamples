import requests

if __name__ == '__main__':
    
    url: str = "https://jsonplaceholder.typicode.com/posts"

    try:

        response = requests.get(url)
        response.raise_for_status()

        data: dict = response.json()

        if isinstance(data, list):
            print("Erfolgreich eine Liste von JSON-Daten erhalten:")
            print(f"Die Liste enthält {len(data)} Elemente.")

            for entry in data:
                print(f"Titel: {entry['title']}")
        else:
            print("Die API liefert keine Liste, sondern:", type(data))
    
    except requests.exceptions.RequestException as e:
        print("Fehler bei der API-Anfrage:", e)

        