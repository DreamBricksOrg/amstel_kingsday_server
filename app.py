from flask import Flask, render_template

import parameters

app = Flask(__name__)

@app.route('/alive')
def home():
    return "alive"

@app.route('/')
def index():
    return render_template('toque_tela.html')

@app.route('/abrircamera')
def abrir_camera():
    return render_template('abrir_camera.html', api_url=parameters.API_URL)

@app.route('/agedenied')
def age_denied():
    return render_template('age_denied.html')

@app.route('/agegate')
def age_gate():
    return render_template('age_gate.html')

@app.route('/agegatedata')
def age_gate_data():
    return render_template('age_gate_data.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/downloadcompartilhar')
def download_compartilhar():
    return render_template('download_compartilhar.html', api_url=parameters.API_URL)

@app.route('/downloadqrcode')
def download_qrcode():
    return render_template('download_qrcode.html')

@app.route('/fotoprocessada')
def foto_processada():
    return render_template('foto_processada.html', api_url=parameters.API_URL)

@app.route('/politicaprivacidade')
def politica_priva():
    return render_template('politica_priva.html')

@app.route('/termosuso')
def termos_uso():
    return render_template('termos_uso.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
