import pickle
import flask
import numpy as np
from flask import request
from sklearn import datasets
from sklearn.metrics import jaccard_similarity_score

app = flask.Flask(__name__)

modelFile = open("./models/iris_model.pkl","rb")
model = pickle.load(modelFile)
testFeatures = pickle.load(open("./data/iris_validation_features.pkl", "rb"))
testClasses = pickle.load(open("./data/iris_validation_classes.pkl", "rb"))

@app.route('/test', methods=['GET'])
def test_model():
    predictions = model.predict(testFeatures)
    score = jaccard_similarity_score(np.array(predictions), np.array(testClasses))
    print(predictions)
    print(testClasses)
    print("score:", score)
    response = {}
    response['predictions'] = predictions.tolist()
    response['truth'] = testClasses.tolist()
    response['score'] = score
    #returning the response object as json
    return flask.jsonify(response)

#defining a route for only post requests
@app.route('/', methods=['POST'])
def prediction():
    #getting an array of features from the post request's body
    features = request.get_json()['features']

    #creating a response object
    #storing the model's prediction in the object
    response = {}
    response['predictions'] = model.predict(features).tolist()

    #returning the response object as json
    return flask.jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
