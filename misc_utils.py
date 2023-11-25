import os
from dotenv import load_dotenv
import constants

def file_exists(path):
    """
    Checks if a file exists at the path specified
    Args:
        path (string): The path to the file
    Returns:
        bool: Returns true if file exists
    """
    return os.path.isfile(path)

def set_intents_env():
    """
    Sets environment variables for the intents and data model so
    that app loads the correct intents and uses the correct data
    model
    Args: None
    Returns:
        tuple (string, string): Returns a tuple of strings. First
                                value is the intents file to use
                                and the second is the data model
                                to use.
    Raises: Raises exception if invalid environment variable value is loaded.
    """
    load_dotenv()
    INTENTS_ENV = os.getenv('INTENTS_ENV')
    if INTENTS_ENV == 'prod': return constants.INTENTS, constants.MODEL_DATA
    if INTENTS_ENV == 'dev': return constants.EXAMPLE_INTENTS, constants.EXAMPLE_MODEL_DATA
    raise Exception("INTENTS_ENV value must be 'prod' or 'dev'")