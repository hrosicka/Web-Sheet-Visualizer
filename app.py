from flask import Flask, render_template, request
import pandas as pd
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file selected'
        file = request.files['file']
        if file.filename == '':
            return 'No file selected'
        if file:
            try:
                df = pd.read_excel(io.BytesIO(file.read()))
                table_html = df.to_html(classes='data-table')
                return render_template('index.html', table_html=table_html)
            except Exception as e:
                return f'Error processing file: {e}'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)