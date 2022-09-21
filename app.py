from flask import Flask, jsonify
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

counts = 0

@app.route('/')
def hello():
    global counts
    counts += 1
    count = redis.incr('hits')
    data = {'text': 'Hello World! I have been seen {} times.'.format(count),
            'counts': counts}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)