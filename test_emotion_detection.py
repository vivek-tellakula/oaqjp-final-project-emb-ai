# Importing emotion_detector function and unittest library
from EmotionDetection.emotion_detection import emotion_detector
import unittest

# Create a testcase class
class TestEmotionDetector(unittest.TestCase):

    # Create a function to run the test cases within the test case class
    def test_emotion_detector(self):
        
        # Call function for required test cases with assertEqual()
        r1 = emotion_detector('I am glad this happened')
        self.assertEqual(r1["dominant_emotion"], 'joy')

        r2 = emotion_detector('I am really mad about this')
        self.assertEqual(r2["dominant_emotion"], 'anger')

        r3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(r3["dominant_emotion"], 'disgust')

        r4 = emotion_detector('I am so sad about this')
        self.assertEqual(r4["dominant_emotion"], 'sadness')

        r5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(r5["dominant_emotion"], 'fear')

# Call the unit tests
unittest.main()