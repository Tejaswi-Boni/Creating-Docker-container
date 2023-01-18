from flask import Flask
from Housing.logger import logging
from Housing.exception import HousingException
import sys


app= Flask(__name__)

@app.route("/",methods = ['GET','POST'])

def index():
    try:
        raise Exception("testing exception module")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("testing logging module")
    return "starting ML project"


if __name__=="__main__":
    app.run(debug=True)