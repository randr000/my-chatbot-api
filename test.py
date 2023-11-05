import unittest
from nltk_utils import tokenize, stem

class TestNLTKUtils(unittest.TestCase):
    def test_tokenize(self):
        """
        Test that a string is properly tokenized
        """
        string = 'What are your favorite programming languages?'
        result = tokenize(string)
        expected = ['What', 'are', 'your', 'favorite', 'programming', 'languages', '?']
        self.assertEqual(result, expected)
    
    def test_stem(self):
        """
        Test that a word is properly stemmed
        """
        words = ['actual', 'Actually', 'ACTUALIZE', 'ACTuaLIzInG']
        result = [stem(word) for word in words]
        expected = ['actual', 'actual', 'actual', 'actual']
        self.assertEqual(result, expected)
        
if __name__ == '__main__':
    unittest.main()