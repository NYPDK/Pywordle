from logging import INFO
import requests

def definition(word):
    req = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=0ac6a912-dc32-4c4f-bbcb-a198cd7ec414")
    info = {"type": req.json()[0]["fl"], "def": req.json()[0]["shortdef"][0]}
    return info

if __name__ == "__main__":
    print(definition("kneel"))