import json
from intents import intents
import constants

# Convert dictionary to json object and write to intents.json
# Only saves to the production intents file so that one doesn't accidently
# save the production intents to the example.intents file
with open(constants.INTENTS, 'w') as f:
    json.dump(intents, f, indent=2)