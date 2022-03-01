# fapp -> shortcut from happy flasker extension
from statistics import mode
from flask import Flask, render_template,request
import numpy as np
from joblib import load

app = Flask(__name__)

def load_clf_model():
	filepath = 'app_1/clf_ap.pkl'
	return load(filepath)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method=="POST":
		form = request.form
		age = int(form.get('age'))
		salary = float(form.get('salary'))
		userinp = np.array([[age,salary]]) 
		model_dict = load_clf_model()
		
		x = model_dict.get('scaler').transform(userinp)
		print(x)
		p = model_dict.get('classifier').predict(x)
		print(p) # will be a single item array
  
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
 