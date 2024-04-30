# train_chatbot.py
import os
import json
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.layers import Input
from keras.optimizers import SGD
import random
import pickle
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize
from datetime import datetime

stemmer = LancasterStemmer()

# Load intents file
with open('intents.json') as file:
    intents = json.load(file)

words = []
classes = []
documents = []
ignore_words = ['?', '!', '.', ',']

# Load intents patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize each word in the sentence
        w = word_tokenize(pattern)
        # Add to our words list
        words.extend(w)
        # Add to documents in our corpus
        documents.append((w, intent['tag']))
        # Add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Training data creation
training = []
output_empty = [0] * len(classes)
for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training, dtype=object)
train_x = list(training[:,0])
train_y = list(training[:,1])

# Model definition
model = Sequential()
model.add(Input(shape=(len(train_x[0]),)))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train model
model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5')

# Save data structures
pickle.dump({'words': words, 'classes': classes, 'train_x': train_x, 'train_y': train_y}, open("training_data", "wb"))

# Function to handle academic calendar
def load_academic_calendar(filename='academic_calendar.json'):
    with open(filename, 'r') as file:
        return json.load(file)

# Additional functions for academic calendar as in ben.py

# Functions for chatbot interaction
def clean_up_sentence(sentence):
    sentence_words = word_tokenize(sentence)
    return [stemmer.stem(word.lower()) for word in sentence_words]

def bow(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)  
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s: 
                bag[i] = 1
    return np.array(bag)

def classify(sentence):
    p = bow(sentence, words)
    res = model.predict(np.array([p]))[0]
    results = [[i, r] for i, r in enumerate(res) if r > 0.25]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = [(classes[r[0]], r[1]) for r in results]
    return return_list

def response(sentence):
    results = classify(sentence)
    if results:
        for i in intents['intents']:
            if i['tag'] == results[0][0]:
                return random.choice(i['responses'])
    return "Sorry, I do not understand."

# Example usage of the chatbot
if __name__ == "__main__":
    user_input = "When is the next exam?"
    print(response(user_input))
