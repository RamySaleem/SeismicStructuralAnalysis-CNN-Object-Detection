from flask import Flask, render_template, request, jsonify
import pickle

tokenizer = pickle.load(open("cv.pkl", "rb"))
model = pickle.load(open("clf.pkl"), "rb")




# from utils import model_predict
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    email = request.form.get('content')
    tokenized_email = cv.transform([email])
    prediction =  model.predict(tokenizer.transform(email_text)) # model_predict(email)
    return render_template("index.html", prediction=prediction, email=email)

# Create an API endpoint
@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)  # Get data posted as a json
    email = data['content']
    prediction = model_predict(email)
    return jsonify({'prediction': prediction, 'email': email})  # Return prediction

if __name__ == "__main__":
    app.run()