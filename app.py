from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def ficha():
  return render_template('index.html')

@app.route('/ficha', methods=['POST'])
def resultado():
  nome = str(request.form['nome'])
  origem = str(request.form['origem'])
  coman = str(request.form['coman'])
  cie = str(request.form['cie'])
  manu = str(request.form['manu'])
  seg = str(request.form['seg'])
  est = str(request.form['est'])
  equip = str(request.form['equip'])
  return render_template('ficha.html',
                         nome = nome,
                         origem = origem,
                         max_com = coman,
                         max_manu = manu,
                         max_cie = cie,
                         max_sec = seg,
                         max_est = est,
                         equipamentos = equip)
