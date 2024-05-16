from flask import Flask, request, jsonify
import json
from flask_cors import CORS
import subprocess

#Ermöglichung CORS (Cross-Origin Resource Sharing)
app = Flask(__name__)
cors = CORS(app, resources={r'/get-game': {'origins': '*'}})

#GET-Request, um die JSON zu erhalten
@app.route("/get-game")
def getGame():
    try:
        with open("C:/Users/Rouven von Lübtow/Lasergame/pythonAPI/Games.json", 'r', encoding='utf-8') as file: #laden der JSON
            game_data = json.load(file)
            return json.dumps(game_data, ensure_ascii=False, indent=4), 200 #zurückschicken der JSON
    except FileNotFoundError:
        return "Die Datei wurde nicht gefunden."
    except json.JSONDecodeError:
        return "Die Datei enthält keine gültigen JSON-Daten."

#POST-Request, um Werte in der JSON zu verändern
@app.route("/set-game/<game_id>", methods=["POST"]) #<game_id> steht für den zu verändernen Wert
def setGame(game_id):
    try:
        with open("C:/Users/Rouven von Lübtow/Lasergame/pythonAPI/Games.json", 'r', encoding='utf-8') as file:
            game_data = json.load(file)
            if(game_id == "Lasergame"):
                game_data['1'] = True
            elif(game_id == "Lichtergame"):
                game_data['2'] = True
                subprocess.call('C:/Users/Rouven von Lübtow/temp/Hinweis1.txt', shell=True)
            elif(game_id == "NFC-Tag"):
                game_data['3'] = True
            elif(game_id == "Anleitung-Lichtergame"):
                game_data['4'] = True
    
        with open("C:/Users/Rouven von Lübtow/Lasergame/pythonAPI/Games.json", 'w', encoding='utf-8') as file: #Öffnen der JSON im Schreibmodus
            json.dump(game_data, file, ensure_ascii=False, indent=4) #schreiben in die JSON-Datei

            return json.dumps(game_data, ensure_ascii=False, indent=4), 200 #Antwort + Statuscode 200
    except FileNotFoundError:
        return "Die Datei wurde nicht gefunden."
    except json.JSONDecodeError:
        return "Die Datei enthält keine gültigen JSON-Daten."


# @app.after_request
# def set_cors_headers(response):
#     response.headers['Acces-Control-Allow-Origin'] = '*'
#     return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

    
