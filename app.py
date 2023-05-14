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
 com = ficha.get("B2")[0][0]
 cie = ficha.get("B3")[0][0]
 man = ficha.get("B4")[0][0]
 sec = ficha.get("B5")[0][0]
 return render_template('ficha.html',
                        nome = nom,
                        max_com = com,
                        max_manu = man,
                        max_cie = cie,
                        max_sec = sec)

@app.route('/ficha2')
def base2():
 nom = ficha.get("C1")[0][0]
 com = ficha.get("C2")[0][0]
 cie = ficha.get("C3")[0][0]
 man = ficha.get("C4")[0][0]
 sec = ficha.get("C5")[0][0]
 return render_template('ficha.html',
                        nome = nom,
                        max_com = com,
                        max_manu = man,
                        max_cie = cie,
                        max_sec = sec)

@app.route('/ficha3')
def base3():
 nom = ficha.get("D1")[0][0]
 com = ficha.get("D2")[0][0]
 cie = ficha.get("D3")[0][0]
 man = ficha.get("D4")[0][0]
 sec = ficha.get("D5")[0][0]
 return render_template('ficha.html',
                        nome = nom,
                        max_com = com,
                        max_manu = man,
                        max_cie = cie,
                        max_sec = sec)

@app.route('/ficha4')
def base4():
 nom = ficha.get("E1")[0][0]
 com = ficha.get("E2")[0][0]
 cie = ficha.get("E3")[0][0]
 man = ficha.get("E4")[0][0]
 sec = ficha.get("E5")[0][0]
 return render_template('ficha.html',
                        nome = nom,
                        max_com = com,
                        max_manu = man,
                        max_cie = cie,
                        max_sec = sec)


@app.route('/')
def resulta():
  perso1 = ficha.get("B1")[0][0]
  perso2 = ficha.get("C1")[0][0]
  perso3 = ficha.get("D1")[0][0]
  perso4 = ficha.get("E1")[0][0]
  nome1 = registros.get("A1")[0][0]
  nome2 = registros.get("A2")[0][0]
  nome3 = registros.get("A3")[0][0]
  nome4 = registros.get("A4")[0][0]
  roll1 = registros.get("B1")[0][0]
  roll2 = registros.get("B2")[0][0]
  roll3 = registros.get("B3")[0][0]
  roll4 = registros.get("B4")[0][0]
  imagem = registros.get("A8")[0][0]
  return render_template('resultados.html',
                         p1 = perso1,
                         p2 = perso2,
                         p3 = perso3,
                         p4 = perso4,
                         n1 = nome1,
                         n2 = nome2,
                         n3 = nome3,
                         n4 = nome4,
                         r1 = roll1,
                         r2 = roll2,
                         r3 = roll3,
                         r4 = roll4,
                        img = imagem)
 
@app.route('/processa', methods=['POST'])
def processar():
 numero = request.form['numero']
 nome = request.form['name']
 registros.insert_row([nome, numero], index=1)
 return "Ok"
