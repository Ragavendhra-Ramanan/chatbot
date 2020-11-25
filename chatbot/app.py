from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
import json
import os
import joblib
import nltk
from nltk.stem.lancaster import LancasterStemmer

app = Flask(__name__)


@app.route('/', methods = ['POST','GET'])
def index():
 stemmer = LancasterStemmer()

 chatbot_model = load_model('final_model.h5')
 scaler = joblib.load('trained.pkl')

 def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        # adds a counter to an iterable and returns it in a form of numbered object
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return np.array(bag)


 return render_template('index.html')

@app.route('/get',methods=['POST','GET'])
def getResponse():
	while True:
		if userInput.lower() == "bye":
			break
		results = model.predict(bag_of_words(userInput, words).reshape(-1,468))
		results_index = np.argmax(results)
		user_tag = labels[results_index]

		if results.max() > 0.85:
			for tag_selection in data['intents']:
				if tag_selection['tag'] == user_tag:
					responses = tag_selection['responses']
			print(random.choice(responses))
		else:
			print("Sorry I didn't get that. Please try again or go to https://worlddatascience.tech/datapedia for more assistance")



if __name__ == '__main__':
   app.run()
