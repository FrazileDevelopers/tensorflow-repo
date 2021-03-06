import json
import tensorflow as tf 
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

with open(r"Data\sarcasm.json", 'r') as f:
    datastore = json.load(f)

sentences = []
labels = []
urls = []

for item in datastore:
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])
    urls.append(item['article_link'])

tokenizer = Tokenizer(oov_token = '<OOV>')
tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index
print(len(word_index))
print(word_index)
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, padding='post')
print(sentences[2])
print(padded[2])
print(padded.shape)

# https://github.com/rishabhmisra/News-Headlines-Dataset-For-Sarcasm-Detection
# https://rishabhmisra.github.io/publications/
# https://storage.googleapis.com/laurencemoroney-blog.appspot.com/sarcasm.json (For list view of json file format)