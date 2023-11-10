import os

def file_exists(path):
    """
    Checks if a file exists at the path specified
    Args:
        path (string): The path to the file
    Returns:
    bool: Returns true if file exists
    """
    return os.path.isfile(path)