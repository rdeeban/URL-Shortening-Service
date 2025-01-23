from flask import Flask, request, jsonify
import short_url
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
SEED = 1

def unique_id():
	global SEED
	uid = SEED
	SEED += 1
	return uid

@app.route('/get-short-url', methods=['POST'])
def get_short_url():
	content = request.json
	long_url = content['URL']
	object_id = unique_id()
	shortened_url = "http://shrtn.me/{}".format(short_url.encode_url(object_id))
	r.set(shortened_url, object_id)
	r.set(object_id, long_url)
	return jsonify({"long_url": long_url, "shortened_url": shortened_url})

@app.route('/get-long-url', methods=['POST'])
def get_long_url():
	content = request.json
	shortened_url = content['URL']
	object_id = r.get(shortened_url)
	long_url = r.get(object_id)
	return jsonify({"long_url": long_url, "shortened_url": shortened_url})

if __name__ == '__main__':
	app.run(debug=True, port=8081)