import xmltodict
import json

if __name__ == '__main__':
    
    data: dict = None
    with open('input.xml') as xml_file:
        data: dict = xmltodict.parse(xml_file.read())

    if data is not None:
        for key, value in data.items():
            print(f"Key={key}, Value={value}")

    if data is not None:
        with open('output.json', 'w') as json_file:
            json_file.write(
                json.dumps(data, indent=4)
            )

        