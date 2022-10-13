from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker
import pandas as pd
import sys
import os
import time
from model import Base, Transaction

def make_session():
    engine=""
    while(not engine):
        try:
            engine = create_engine(os.environ.get('POSTGRESQL_URL'))
            # Creating Database If Not Exists
            if not database_exists(engine.url):
                create_database(engine.url)
        except:
            print(f"Trying to Connect to DB {engine}")
            time.sleep(10)
    try:
        if sys.argv[1]=='--restart':
            Base.metadata.drop_all(engine)
    except IndexError:
        pass
    except:
        print("Error Cleaning DB")
    Base.metadata.create_all(engine)
    Session=sessionmaker(bind=engine)
    s = Session()
    return s


app = Flask(__name__)

s = make_session()

@app.route('/')
def home():
    tuples=s.query(Transaction).order_by(Transaction.id.desc())
    return render_template('home.html',tuples=tuples)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)