from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    dat=pd.read_csv('processed.csv')
    return render_template('home.html',table=dat[['Time','Result']].to_html())

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)