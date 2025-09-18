# test_emotion_detection.py

from EmotionDetection import emotion_detector

# Test statements and expected dominant emotions
tests = {
    "I am glad this happened": "joy",
    "I am really mad about this": "anger",
    "I feel disgusted just hearing about this": "disgust",
    "I am so sad about this": "sadness",
    "I am really afraid that this will happen": "fear"
}

# Run tests
for statement, expected in tests.items():
    result = emotion_detector(statement)
    dominant_emotion = result['dominant_emotion']
    print(f"Text: '{statement}'")
    print(f"Expected: {expected}, Detected: {dominant_emotion}")
    print("PASS" if dominant_emotion == expected else "FAIL")
    print("-" * 40)
