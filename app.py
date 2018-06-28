
from flask import Flask,render_template,flash,request,redirect,url_for,jsonify
import requests

app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
## generate your own hash key
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/eurofy',methods=["POST"])
def eurofy():
	sym=request.form.get('currency').strip().upper()
	try:        ### get your free api key from fixer.io
		res=requests.get(f"http://data.fixer.io/api/latest?access_key=444d148a4a0295a7d982ee9edd55933a&base=EUR&symbols={sym}")
	except:
		return jsonify({"success":0})
	if(res.status_code!=200):
		
		return jsonify({"success":0})
	data=res.json()

	if(data["success"]==False):

		return jsonify({"success":1})
	elif(sym==""):
 		return jsonify({"success":2})

	return jsonify({"success":"OK","rate":data["rates"][sym]})
if __name__=="__main__":
	app.run(debug=True)	
	
