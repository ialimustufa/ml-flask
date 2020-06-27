from flask import Flask , render_template ,request
from flask_ngrok import run_with_ngrok
from sklearn.preprocessing import StandardScaler
import pickle

app  = Flask(__name__)
run_with_ngrok(app)
model = pickle.load(open('model.pkl','rb'))
sc=StandardScaler()

@app.route('/')
def index():
    return render_template('index.html',data="null")

@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
      gender = request.form['gender']
      age= request.form['age']
      sal= request.form['sal']
      
      data=[[int(gender),int(age),int(sal)]]
      p=model.predict(sc.fit_transform(data))
      if p[0]==1:
          prediction="User will purchase product"
      else:
          prediction="User won't purchase product"

      return render_template('index.html',prediction="Prediction: "+prediction)

if __name__=='__main__':
    app.run()