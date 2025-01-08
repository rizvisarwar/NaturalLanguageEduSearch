import unittest
from nlp_example.processor import SentenceProcessor

class TestSentenceProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = SentenceProcessor()

    def test_process(self):
        sentence = "I want to do a Masters on Information Security in Stockholm Sweden."
        what, field_of_study, location = self.processor.process(sentence)
        self.assertEqual(what, "Masters")
        self.assertEqual(field_of_study, "Information Security")
        self.assertEqual(location, "Stockholm Sweden")

if __name__ == '__main__':
    unittest.main()