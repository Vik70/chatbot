# main.py
# Import necessary modules from other files
from preprocessing import preprocess_text
from classifier import train_classifier, predict_intent
from responses import handle_intent, personalize_greeting, conversational_marker, suggest_next_steps, track_progress
import nltk
import logging

# Download necessary resources for NLTK
nltk.download('stopwords')
nltk.download('punkt')

# Initialize logging for debugging
logging.basicConfig(level=logging.INFO)

# Initialize personalized user data
user_data = {"name": None, "preferred_service": None}

# Train the classifier upon running the main script
train_classifier()

# Simulate user interaction
print("Welcome! I can help you with budget inquiries, service types, and consultation details.")
if not user_data["name"]:
    user_data["name"] = input("Chatbot: What’s your name? ")

print(personalize_greeting())
while True:
    user_input = input(f"{user_data['name']}: ")
    if user_input.lower() == "exit":
        print("Chatbot: Thank you! Looking forward to working with you.")
        break

    # Predict intent and log the process
    intent = predict_intent(user_input)
    logging.info(f"Recognized intent: {intent}")

    # Generate response based on intent
    response = handle_intent(intent, user_input)
    logging.info(f"Response generated: {response}")

    # Check progress and conversational markers
    marker = conversational_marker()
    progress = track_progress()

    # Display chatbot's responses
    print(f"Chatbot: {response}")
    if marker:
        print(f"Chatbot: {marker}")
    if progress:
        print(f"Chatbot: {progress}")

    # Suggest next steps
    print(suggest_next_steps())

    # Log transaction progress
    logging.info(f"Transaction status: {progress}")