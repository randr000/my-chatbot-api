# My Chatbot API

## Project Description
I have a portfolio webiste and also wanted to learn more about NLP and machine learning. So I thought it would be a good idea to create a chatbot for it. I relied on the instructions provided in the videos by <a href="https://twitter.com/patloeber" target="_blank">Patrick Loeber</a> located <a href="https://www.youtube.com/playlist?list=PLqnslRFeH2UrFW4AUgn-eY37qOAWQpJyg" target="_blank">here</a> and <a href="https://www.youtube.com/watch?v=a37BL0stIuM&t=913s" target="_blank">here</a>. I used the data from my portfolio resume site located <a href="https://randr000.github.io/portfolio-resume" target="_blank">here</a> to train my bot.

### Training Data
The patterns and responses for the intents are defined in a json file. By default, the example.intents.json file is used when the INTENTS_ENV environment variabe is set to 'dev' and the intents.json file is used when the INTENTS_ENV environment variable is set to 'prod'. The default file names can be changed in the constants.py file. The model is saved in the example.data.pth or data.pth file if the INTENTS_ENV environment variable is set to 'dev' or 'prod'. I included the intents.json and data.pth file in the .gitignore file in order to keep my training data and model private.

In order to make editing the intents file easier, I created an intents.py file where I store the intents in a python dictionary. This file is also in the .gitignore file but I did create an example.intents.py file so one can see how it should be set up. I then run the python script intents_to_json.py to convert the dictionary into json and save it to the intents.json file by typing the following in the terminal:

<code>python3 intents_to_json.py</code>

### Chatbot
The chatbot is trained using a bag-of-words model. It is also stateless which means it will not remember what you previously wrote to determine a response. The bot is also not storing conversations anywhere and is not being trained with the text a user inputs.