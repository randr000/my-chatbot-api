import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from misc_utils import file_exists, set_intents_env

INTENTS_FILE, DATA_FILE = set_intents_env()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

if file_exists(INTENTS_FILE):
    with open(INTENTS_FILE, 'r') as f:
        intents = json.load(f)
else: raise Exception(f'The intents file named {INTENTS_FILE} cannot be found.')

if file_exists(DATA_FILE):
    data = torch.load(DATA_FILE)
else: raise Exception(f'The data model at {DATA_FILE} cannot be found.')

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Raul AI"

def get_response(msg):

    
        sentence = tokenize(msg)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X)

        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent['tag']:
                    return random.choice(intent["responses"])
        return ['I do not understand...']
        

if __name__ == '__main__':
    print("Let's chat! type 'quit' to exit")
    while True:
        sentence = input('You: ')
        if sentence == 'quit':
            break
        for s in get_response(sentence): print(s)