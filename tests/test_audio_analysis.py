import unittest
from src.audio_analysis import load_audio, get_beats

class TestAudioAnalysis(unittest.TestCase):
    def test_load_audio(self):
        y, sr = load_audio("data/audio/sample.mp3")
        self.assertIsNotNone(y)
        self.assertTrue(sr > 0)
