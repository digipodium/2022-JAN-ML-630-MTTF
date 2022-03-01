# fapp -> shortcut from happy flasker extension
from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    form = request.form
    print(form.get('age'))
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
 