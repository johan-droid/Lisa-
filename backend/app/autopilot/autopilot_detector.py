import re
from app.judicial.judicial_brain import JudicialBrain

class AutopilotDetector:
    def __init__(self):
        self.judicial_brain = JudicialBrain()

    def detect(self, text: str) -> bool:
        mode = self.judicial_brain.select_mode(text)
        return mode == "autopilot"

    def detect_spike(self, text: str) -> bool:
         mode = self.judicial_brain.select_mode(text)
         return mode == "spike"

    def get_mode(self, text: str) -> str:
        return self.judicial_brain.select_mode(text)
