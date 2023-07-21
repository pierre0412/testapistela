import requests

r = requests.get('https://stela3k.sictiam.fr/api/acte/public?limit=0&offset=0&direction=&column=&siren=210600979')
dictionnaire = r.json()

dictionnaire = dictionnaire.get("results")

for i in dictionnaire:
    # print(i)
    if i.get("acteAttachment").get("filename").endswith("pdf"):
        print(f'{i.get("decision")} / {i.get("nature")} /  {i.get("objet")} / {i.get("acteAttachment").get("filename")} '
              f'https://stela3k.sictiam.fr/api/acte/public/{i.get("uuid")}/file/stamped')

# ajout de commentaire test
