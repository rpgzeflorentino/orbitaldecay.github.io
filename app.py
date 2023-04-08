from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def ficha():
  return render_template('index.html')

@app.route('/ficha', methods=['POST'])
def resultado():
  varnome = str(request.form['nome'])
  varorigem = str(request.form['origem'])
  varcoman = str(request.form['coman'])
  varcie = str(request.form['cie'])
  varmanu = str(request.form['manu'])
  varseg = str(request.form['seg'])
  varequip = str(request.form['equip'])
  return render_template('ficha.html',
                         nome = varnome,
                         origem = varorigem,
                         max_com = varcoman,
                         max_manu = varmanu,
                         max_cie = varcie,
                         max_sec = varseg,
                         equipamentos = equip)
