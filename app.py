from dotenv import load_dotenv
from flask import Flask, render_template
import os
import parameters
import threading

from log_sender import process_csv_and_send_logs, csv_filename, backup_filename, init_csv, save_csv_additional

app = Flask(__name__)
load_dotenv()

init_csv(csv_filename)
init_csv(backup_filename)

threading.Thread(target=process_csv_and_send_logs, args=(csv_filename, backup_filename), daemon=True).start()


@app.route('/alive')
def home():
    return "alive"

@app.route('/')
def index():
    return render_template('toque_tela.html')

@app.route('/tablet/')
def tablet_index():
    return render_template('toque_tela.html')

@app.route('/abrircamera')
def abrir_camera():
    return render_template('abrir_camera.html', api_url=parameters.API_URL)

@app.route('/tablet/abrircamera')
def tablet_abrir_camera():
    return render_template('abrir_camera.html', api_url=parameters.API_URL)

@app.route('/kingorqueen')
def king_or_queen():
    return render_template('king_or_queen.html')

@app.route('/tablet/kingorqueen')
def tablet_king_or_queen():
    return render_template('king_or_queen.html')

@app.route('/agedenied')
def age_denied():
    save_csv_additional("MENOR_IDADE", "WEB")
    return render_template('age_denied.html')

@app.route('/tablet/agedenied')
def tablet_age_denied():
    save_csv_additional("MENOR_IDADE", "TABLET")
    return render_template('age_denied.html')

@app.route('/agegate')
def age_gate():
    return render_template('age_gate.html')

@app.route('/tablet/agegate')
def tablet_age_gate():
    return render_template('age_gate.html')

@app.route('/agegatedata')
def age_gate_data():
    return render_template('age_gate_data.html')

@app.route('/tablet/agegatedata')
def tablet_age_gate_data():
    return render_template('age_gate_data.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/tablet/download')
def tablet_download():
    return render_template('download.html')

@app.route('/downloadcompartilhar')
def download_compartilhar():
    return render_template('download_compartilhar.html', api_url=parameters.API_URL, api_log=parameters.LOG_API, api_log_project=parameters.LOG_PROJECT_ID)

@app.route('/tablet/downloadcompartilhar')
def tablet_download_compartilhar():
    return render_template('download_compartilhar.html', api_url=parameters.API_URL)

@app.route('/downloadqrcode')
def download_qrcode():
    return render_template('download_qrcode.html', api_url=parameters.API_URL)

@app.route('/tablet/downloadqrcode')
def tablet_download_qrcode():
    return render_template('download_qrcode.html', api_url=parameters.API_URL)

@app.route('/fotoprocessada')
def foto_processada():
    save_csv_additional("FOTO_GERADA", "WEB")
    return render_template('foto_processada.html', api_url=parameters.API_URL)

@app.route('/tablet/fotoprocessada')
def tablet_foto_processada():
    save_csv_additional("FOTO_GERADA", "TABLET")
    return render_template('foto_processada.html', api_url=parameters.API_URL)

@app.route('/politicaprivacidade')
def politica_priva():
    return render_template('politica_priva.html')

@app.route('/tablet/politicaprivacidade')
def tablet_politica_priva():
    return render_template('politica_priva.html')

@app.route('/termosuso')
def termos_uso():
    return render_template('termos_uso.html')

@app.route('/tablet/termosuso')
def tablet_termos_uso():
    return render_template('termos_uso.html')

@app.route('/tablet/qrcodescanned')
def qrcode_scanned():
    save_csv_additional("ESCANEOU", "TABLET")
    return render_template('qrcode_scanned.html',api_url=parameters.API_URL, api_log=parameters.LOG_API, api_log_project=parameters.LOG_PROJECT_ID)

if __name__ == '__main__':
    context = ('fullchain.pem', 'privkey.pem')
    if os.getenv('LOCAL_SERVER'):
        app.run(debug=True, host='0.0.0.0')
    else:
        app.run(host='0.0.0.0', ssl_context=context)
