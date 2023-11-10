import unittest
from nltk_utils import tokenize, stem, bag_of_words

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
    
    def test_bag_of_words(self):
        """
        Test that a tokenized sentence is properly converted into a bag of words
        """
        tokenized_sentence = ["the", "dog", "fetched", "a", "ball"]
        all_words = [stem(w) for w in ["the", "cat", "dog", "mouse", "fetched", "yarn", "cheese", "ball"]]
        result = bag_of_words(tokenized_sentence, all_words)
        expected = [1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0]
        self.assertListEqual(result.tolist(), expected)
        
if __name__ == '__main__':
    unittest.main()