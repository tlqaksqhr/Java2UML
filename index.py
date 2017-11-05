from flask import *
from lib.Java2UML import Java2UML

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/java2uml',methods = ['GET','POST'])
def java2uml():
	MainClass = Java2UML()

	if request.method == 'POST':
		code = request.form['code']
	else:
		code = request.args.get('code')

	result = MainClass.JavaCode2UML(code)
	result.replace("\n","\r\n")
	
	return result

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=30000)