from flask import Flask, render_template
from joblib import load
from requests import request

app = Flask(__name__)

def loadModel():
    path='Apps\Linear Regression\RandomForest\static\house_pricing_model.pk'
    model_dict=load(path)
    return model_dict

@app.route('/')
def index():
    md= loadModel()
    cities=md['Cities']
    resident= md['Resident']
    scaler=md['Scaler']
    city_enc=md['City Encoder']
    resident_enc=md['Resident Encoder']
    model=md['Model']

    if request.method=='POST':
        city=request.form['city']
        beds=request.form['beds']
        baths=request.form['baths']
        rt=request.form['res_type']
        size=request.form['sqft']

        if beds.isnumeric() and baths.isnumeric() and size.isnumeric():
            beds=int(beds)
            baths= int(baths)
            size= int(size)
            predicted_price=
    return render_template('index.html', cities= cities, residents=resident)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 