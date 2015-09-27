from flask import Flask, request,jsonify
from lolmax import predict,getlat

app = Flask(__name__)
#app.debug=True

@app.route('/data/<lol>',methods=['GET'])
def app_data(lol):
	j=[]
	j=predict(lol)
	return jsonify(predict=j)

@app.route('/getlocation/<lolmax>',methods=['GET'])
def applol(lolmax):
	j=[]
	j=getlat(lolmax)
	
	return jsonify(position=j)


if __name__ == '__main__':
  app.run(host="0.0.0.0",port=12345)