from flask import Flask, render_template, request
import pandas as pd
import io
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Nebyl vybrán žádný soubor.'
        file = request.files['file']
        if file.filename == '':
            return 'Nebyl vybrán žádný soubor.'
        if file:
            filename = secure_filename(file.filename) #Bezpečnost
            if not filename.endswith(('.xls', '.xlsx')):
                return 'Neplatný formát souboru. Nahrajte prosím Excel soubor.'
            try:
                df = pd.read_excel(io.BytesIO(file.read()))
                table_html = df.to_html(classes='data-table')
                return render_template('index.html', table_html=table_html)
            except Exception as e:
                return f'Chyba při zpracování souboru: {e}'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)