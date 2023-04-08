from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def ficha():
  return render_template('index.html')

@app.route('/ficha', methods=['POST'])
def resultado():
  varnome = str(request.form['nome'])
  varorigem = str(request.form['origem'])
  varcoman = int(request.form['coman'])
  varcie = int(request.form['cie'])
  varmanu = int(request.form['manu'])
  varseg = int(request.form['seg'])
  varequip = int(request.form['equip'])
  return render_template('ficha.html',
                         nome = varnome,
                         origem = varorigem,
                         max_com = varcoman,
                         max_manu = varmanu,
                         max_cie = varcie,
                         max_sec = varseg,
                         equipamentos = varequip)
