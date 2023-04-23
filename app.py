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
ficha1 = planilha.worksheet("ficha1")

@app.route('/ficha1')
def ficha1():
 nom = ficha1.get("B1")[0][0]
 ori = ficha1.get("B2")[0][0]
 com = ficha1.get("B3")[0][0]
 cie = ficha1.get("B4")[0][0]
 man = ficha1.get("B5")[0][0]
 sec = ficha1.get("B6")[0][0]
 return render_template('ficha.html',
                        nome = nom,
                        origem = ori,
                        max_com = com,
                        max_manu = man,
                        max_cie = cie,
                        max_sec = sec)


@app.route('/resultados')
def resulta():
  nome1 = str(registros.get("A1")[0][0])
  nome2 = str(registros.get("A2")[0][0])
  nome3 = str(registros.get("A3")[0][0])
  nome4 = str(registros.get("A4")[0][0])
  roll1 = int(registros.get("B1")[0][0])
  roll2 = int(registros.get("B2")[0][0])
  roll3 = int(registros.get("B3")[0][0])
  roll4 = int(registros.get("B4")[0][0])
  return render_template('resultados.html',
                         n1 = nome1,
                         n2 = nome2,
                         n3 = nome3,
                         n4 = nome4,
                         r1 = roll1,
                         r2 = roll2,
                         r3 = roll3,
                         r4 = roll4)



@app.route('/ficha', methods=['POST'])
def resultado():
  varnome = str(request.form['nome'])
  varorigem = str(request.form['origem'])
  varcoman = int(request.form['coman'])
  varcie = int(request.form['cie'])
  varmanu = int(request.form['manu'])
  varseg = int(request.form['seg'])
  varequip = str(request.form['equip'])
  return render_template('ficha.html',
                         nome = varnome,
                         origem = varorigem,
                         max_com = varcoman,
                         max_manu = varmanu,
                         max_cie = varcie,
                         max_sec = varseg,
                         equipamentos = varequip)


