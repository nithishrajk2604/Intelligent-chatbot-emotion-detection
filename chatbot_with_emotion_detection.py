# chatbot_with_emotion_detection.py

import random
import nltk
from transformers import pipeline

# Download NLTK's required data
nltk.download('punkt')

# Predefined chatbot responses
responses = [
    "Hello! How can I assist you today?",
    "I'm here to help you.",
    "What can I do for you?",
    "Tell me more about it."
]

# Function to get a random chatbot response
def chatbot_response():
    return random.choice(responses)

# Emotion detection pipeline (pre-trained model)
emotion_detector = pipeline("sentiment-analysis")

def detect_emotion(user_input):
    result = emotion_detector(user_input)[0]
    return result['label'], result['score']

def main():
    print("Welcome to the Intelligent Chatbot with Emotion Detection!")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        # Get emotion from user input
        emotion, confidence = detect_emotion(user_input)
        
        # Get chatbot response
        chatbot_reply = chatbot_response()
        
        # Print output
        print(f"Chatbot: {chatbot_reply}")
        print(f"Emotion detected: {emotion} (Confidence: {confidence:.2f})")

if __name__ == "__main__":
    main()
