from flask import Flask,render_template,request
import pickle
import numpy as np


model = pickle.load(open('/home/pushpendra/Desktop/Env/flaskenv/Model.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def fun():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    # values = [int(x) for x in request.form.values()]
    ram=int(request.form.get('ram'))
    rom=int(request.form.get('rom'))
    size=float(request.form.get('size'))
    primary=int(request.form.get('primary'))
    selfi=int(request.form.get('selfi'))
    battery=int(request.form.get('battery'))
    values=[ram,rom,size,primary,selfi,battery]
    final=np.array(values)
    prediction=model.predict(final.reshape(1,-1))
    output=prediction[0]
    return  render_template('index.html',sent_value=f"Enpected price of phone is {output}")

if __name__=="__main__":
    app.run(debug=True)