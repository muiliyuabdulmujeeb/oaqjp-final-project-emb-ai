import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        first_response = emotion_detector("I am glad this happened")
        second_response = emotion_detector("I am really mad about this")
        third_response = emotion_detector("I feel disgusted just hearing about this")
        fourth_response = emotion_detector("I am so sad about this")
        fifth_response = emotion_detector("I am really afraid that this will happen")

        assert first_response["dominant_emotion"] == "joy"
        assert second_response["dominant_emotion"] == "anger"
        assert third_response["dominant_emotion"] == "disgust"
        assert fourth_response["dominant_emotion"] == "sadness"
        assert fifth_response["dominant_emotion"] == "fear"


unittest.main()