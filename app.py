from flask import Flask,render_template,request
import pickle
app=Flask(__name__)
#load the module
model=pickle.load(open('savedmodel.sav','rb'))
@app.route('/')
def home():
    result = " "
    return render_template('home.html',**locals())

@app.route('/predict',methods=['POST','GET'])
def predict():
    Sepal_Length=float(request.form['Sepal_Length'])
    Sepal_Width=float(request.form['Sepal_Width'])
    Petal_Length=float(request.form['Petal_Length'])
    Petal_Width=float(request.form['Petal_Width'])

    result  = model.predict([[Sepal_Length,Sepal_Width,Petal_Length,Petal_Width]])[0]
    return render_template('home.html',**locals())

if __name__ == '__main__':
    app.run(debug=True)