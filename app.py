from flask import Flask, request, render_template
import gspread
import json
import requests
import os
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

GOOGLE_SHEETS_CREDENTIALS = os.environ['GOOGLE_SHEETS_CREDENTIALS']
with open('credenciais.json', mode = "w") as arquivo:
 arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json')

api = gspread.authorize(conta)
planilha = api.open_by_key("1TeH6cHH4-qDHFHfQT-NtqjaYzSLO4BdyDs6GQyxdAAk")
registros = planilha.worksheet("resultados")
ficha = planilha.worksheet("fichas")

@app.route('/ficha1')
def base1():
 nom = ficha.get("B1")[0][0]
 ori = ficha.get("B2")[0][0]
 com = ficha.get("B3")[0][0]
 cie = ficha.get("B4")[0][0]
 man = ficha.get("B5")[0][0]
 sec = ficha.get("B6")[0][0]
 return render_template('ficha.html',
                        nome = nom,
                        origem = ori,
                        max_com = com,
                        max_manu = man,
                        max_cie = cie,
                        max_sec = sec)

@app.route('/ficha2')
def base2():
 nom = ficha.get("C1")[0][0]
 ori = ficha.get("C2")[0][0]
 com = ficha.get("C3")[0][0]
 cie = ficha.get("C4")[0][0]
 man = ficha.get("C5")[0][0]
 sec = ficha.get("C6")[0][0]
 return render_template('ficha.html',
                        nome = nom,
                        origem = ori,
                        max_com = com,
                        max_manu = man,
                        max_cie = cie,
                        max_sec = sec)

@app.route('/ficha3')
def base3():
 nom = ficha.get("D1")[0][0]
 ori = ficha.get("D2")[0][0]
 com = ficha.get("D3")[0][0]
 cie = ficha.get("D4")[0][0]
 man = ficha.get("D5")[0][0]
 sec = ficha.get("D6")[0][0]
 return render_template('ficha.html',
                        nome = nom,
                        origem = ori,
                        max_com = com,
                        max_manu = man,
                        max_cie = cie,
                        max_sec = sec)

@app.route('/ficha4')
def base4():
 nom = ficha.get("E1")[0][0]
 ori = ficha.get("E2")[0][0]
 com = ficha.get("E3")[0][0]
 cie = ficha.get("E4")[0][0]
 man = ficha.get("E5")[0][0]
 sec = ficha.get("E6")[0][0]
 return render_template('ficha.html',
                        nome = nom,
                        origem = ori,
                        max_com = com,
                        max_manu = man,
                        max_cie = cie,
                        max_sec = sec)


@app.route('/')
def resulta():
  nome1 = registros.get("A1")[0][0]
  nome2 = registros.get("A2")[0][0]
  nome3 = registros.get("A3")[0][0]
  nome4 = registros.get("A4")[0][0]
  roll1 = registros.get("B1")[0][0]
  roll2 = registros.get("B2")[0][0]
  roll3 = registros.get("B3")[0][0]
  roll4 = registros.get("B4")[0][0]
  return render_template('resultados.html',
                         n1 = nome1,
                         n2 = nome2,
                         n3 = nome3,
                         n4 = nome4,
                         r1 = roll1,
                         r2 = roll2,
                         r3 = roll3,
                         r4 = roll4)

@app.route('/processa')
def processado():
 nome_personagem = 'José'
 numero_sorteado = 1
 registros.insert_row([nome_personagem, numero_sorteado], index=1)
 return "Ok"
