from flask import Flask
import config

app = Flask(__name__)


# APi to return the stored message in memory and than flush them out
@app.route('/api/<string:topic>', methods=['GET'])
def get_data(topic):
    if config.data_received[topic]:
        data = config.data_received[topic]
        config.data_received[topic] = []
        return {"message": data}, 200
    else:
        return {"message": "Data not found"}, 404


if __name__=="__main__":
    app.run()
