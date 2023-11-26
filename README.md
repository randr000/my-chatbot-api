# My Chatbot API

## Project Description
I have a portfolio webiste and also wanted to learn more about NLP and machine learning. So I thought it would be a good idea to create a chatbot for it. I relied on the instructions provided in the videos by <a href="https://twitter.com/patloeber" target="_blank">Patrick Loeber</a> located <a href="https://www.youtube.com/playlist?list=PLqnslRFeH2UrFW4AUgn-eY37qOAWQpJyg" target="_blank">here</a> and <a href="https://www.youtube.com/watch?v=a37BL0stIuM&t=913s" target="_blank">here</a>. I used the data from my portfolio resume site located <a href="https://randr000.github.io/portfolio-resume" target="_blank">here</a> to train my bot.

### Training Data
The patterns and responses for the intents are defined in a json file. By default, the example.intents.json file is used when the INTENTS_ENV environment variabe is set to 'dev' and the intents.json file is used when the INTENTS_ENV environment variable is set to 'prod'. The default file names can be changed in the constants.py file.